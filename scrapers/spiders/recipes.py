import scrapy
import json

class RecipeSpider(scrapy.Spider):
    name = "recipes"

    BASEURL = "http://www.epicurious.com"

    def start_requests(self):

        # with open('../all_links.json') as f:
        #     items = json.load(f)
        with open('all_links.json') as f:
            items = json.load(f)

        urls = []
        for item in items:
            urls.append(
                self.BASEURL + item["link"]
            )
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        active_time = None
        total_time = None
        ingredients = []
        link = response.url

        # Extract things
        try:
            active_time = response.xpath('//dd[@class="active-time"]/text()').extract()[0]
        except:
            pass
        try:
            total_time = response.xpath('//dd[@class="total-time"]/text()').extract()[0]
        except:
            pass
        ingredients = response.css('li.ingredient').xpath('text()').extract()

        yield {
            "active time": active_time,
            "total time": total_time,
            "ingredients": ingredients,
            "url": link
        }

