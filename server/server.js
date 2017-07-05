var express = require('express');
var sqlite3 = require('sqlite3').verbose();
var bodyParser = require('body-parser');

var app = express();
app.use(bodyParser.urlencoded({extended: true}));

// ALLOW CORS 

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// CONNECT TO (SQLITE) DATABASE 

function giveDBConnection(dbname) {
    var dbObj = new sqlite3.Database(dbname, sqlite3.OPEN_READWRITE, function(err){
        if(err) console.log(err);
    });
    console.log("Connected to data.db");
    return(dbObj);
}

myDB = giveDBConnection("data.db");

// REST CALLS

app.get("/", function(req, res){
    console.log("TEST CONNECTION PLEASE IGNORE: CONNECTION WORKS!");
});

// -- Find id'erne på de ingredienser der indgår i opskrift 123
// SELECT ingredient_id FROM relationship where recipe_id = 123;

// -- Find navnene på de ingredienser der indgår i opskrift 1
// SELECT ingredients.name FROM ingredients LEFT JOIN relationship ON ingredients.id=relationship.ingredient_id WHERE relationship.recipe_id = 1;

// -- Find id'erne på de opskrifter hvor ingrediens 1, 4 og 7 indgår
// SELECT recipes.id FROM recipes INNER JOIN relationship ON recipes.id=relationship.recipe_id WHERE relationship.ingredient_id IN (1, 4, 7) GROUP BY recipes.id HAVING COUNT(DISTINCT relationship.ingredient_id) = 3;

// SERVER

var server = app.listen(3000, function(){
    var port = server.address().port;
    console.log("Listening on port %s", port);
})

