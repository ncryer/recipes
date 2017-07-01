import scrapy

class RecipeLinkSpider(scrapy.Spider):
    """
    Crawl the recipe index and check for new recipes

    recipe index : http://www.epicurious.com/search/?special-consideration=vegetarian%2Cvegan
    """
    name = "Links"
    BASEURL = "http://www.epicurious.com/search/?special-consideration=vegetarian%2Cvegan&content=recipe&page={}"
    ctr = 2

    def start_requests(self):
        urls = [self.BASEURL.format(self.ctr)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ Get list of available recipes on the page
            by [name, href]
        """

        recipes = response.xpath('//h4[@class="hed"]/a')
        for recipe in recipes:
            name = recipe.xpath('text()').extract()[0]
            href = recipe.xpath('@href').extract()[0]
            yield {
                'name': name,
                'link': href
            }

        # Go to next page
        self.ctr += 1
        if self.ctr < 179:
            next_page = self.BASEURL.format(self.ctr)
            yield scrapy.Request(url=next_page, callback=self.parse)