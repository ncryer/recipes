# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:28:05 2017

@author: NICR
"""
import json
import sqlite3

with open("recipes_weighted.json", "r") as f:
    recipes = json.load(f)
                    
# Connect to DB 
connection = sqlite3.connect("../server/data.db")
cursor = connection.cursor()

for recipe in recipes:
    w_tot = 0
    for thing in recipe["ingredients"]:
        w_tot += thing["weight"]
    
    recipe_name = recipe["name"]
    recipe_url = recipe["url"]
    
    cursor.execute('''INSERT INTO recipes (name, url, total_weight) VALUES (?, ?, ?)''', 
                   (recipe_name, recipe_url, w_tot))
    recipe_id = cursor.lastrowid
    for ingredient in recipe["ingredients"]:
        if not "name" in ingredient:
            continue
        cursor.execute('''SELECT id FROM ingredients WHERE name = ? ''', (ingredient["name"],))
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute('''INSERT INTO ingredients (name, weight) VALUES (?, ?)''', (ingredient["name"], ingredient["weight"]))
            ingredient_id = cursor.lastrowid
        else:
            # Ingredient found!
            ingredient_id = rows[0][0]
        # Insert relationship
        cursor.execute('''INSERT INTO relationship (recipe_id, ingredient_id) VALUES (?, ?)''', (recipe_id, ingredient_id))
connection.commit()
connection.close()
