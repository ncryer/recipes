CREATE TABLE recipes (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       url TEXT NOT NULL,
       total_weight NUMBER NOT NULL
);

CREATE TABLE ingredients (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       weight NUMBER NOT NULL
);

CREATE TABLE relationship (
       recipe_id INTEGER NOT NULL,
       ingredient_id INTEGER NOT NULL
);
