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
    return(dbObj)
}

myDB = giveDBConnection("");

// REST CALLS

app.get("/", function(req, res){
    console.log("Connected");
});

// ... fill in with queries

// SERVER

var server = app.listen(3000, function(){
    var port = server.address.port;
    console.log("Listening on port %s", port);
})

