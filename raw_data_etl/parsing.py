import json
import os

os.chdir("C:\\Users\\nicr\\Desktop\\Projects\\recipes")
with open("recipes.json") as f:
    recipes = json.load(f)


def get_title(url):
    this_url = url.split("/")[-1]
    return this_url.replace("-", " ")

os.chdir("C:\\Users\\nicr\\Desktop\\Projects\\recipes\\json")
json_recipes = os.listdir(os.getcwd())


outgoing_json = []
for i in range(len(json_recipes)):
    fname = "r{}.json".format(i)
    with open(json_recipes[i]) as parsed_file:
        this_recipe = json.load(parsed_file)
        
        recipe_title = get_title(recipes[i]["url"])
        recipe_url = recipes[i]["url"]
        
        recipe_json = {
                "name":recipe_title,
                "url":recipe_url, 
                "ingredients": this_recipe
                }
        outgoing_json.append(recipe_json)

with open("recipe_aggregate.json", "w") as f:
    json.dump(outgoing_json, f)