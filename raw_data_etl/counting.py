# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:29:27 2017

@author: NICR
"""

import json
from nltk.probability import FreqDist

with open("recipe_aggregate.json") as f:
    recipes = json.load(f)

ingredients = []
faults = []
for recipe in recipes:
    all_ingredients = recipe["ingredients"]
    for thing in all_ingredients:
        try:
            ingredients.append(thing["name"])
        except KeyError:
            faults.append(thing)
            

fdist = FreqDist(ingredients)

# Compute proportion of occurrence in recipes 

ingredient_weights = {}
unique_ingredients = list(set(ingredients))
N = len(unique_ingredients)

for ingredient in unique_ingredients:
    ingredient_weights[ingredient] = fdist[ingredient] / N

# update recipe struct

for recipe in recipes:
    for thing in recipe["ingredients"]:
        try:
            weight = ingredient_weights[thing["name"]]
        except:
            weight = 0
        thing["weight"] = weight

with open("recipes_weighted.json", "w") as f:
    json.dump(recipes, f)