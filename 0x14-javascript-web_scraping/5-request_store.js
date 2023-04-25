#!/usr/bin/node
/*Script that gets the content of a web page and save it in a file*/
const request = require('request');
const fs = require('fs');
webUrl = process.argv[2];
filePath = process.argv[3];

request(webUrl, function(error, response, body) {
    if (error) {
        console.log(error);
    }
    body = JSON.parse(body)
    fs.writeFile(filePath, body, 'utf-8', err => {
        if (err) {
            console.log(err);
        }
    });
});
