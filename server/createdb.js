var fs = require("fs");
var sqlite3 = require("sqlite3").verbose();

var db = new sqlite3.Database("data.db");

fs.readFile("schema.sql", "ascii", (err, data) => {
    if (err) {
        return console.log(err);
    }
    console.log("Schema read OK");
    db.exec(data, (err) => {
        if (err) {
            return console.log(err);
        }
        console.log("Tables created OK");
    });
});
