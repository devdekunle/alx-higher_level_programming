#!/usr/bin/node
// a script to write a string into a file

const fs = require('fs');
filePath = process.argv[2];
stringToStore = process.argv[3];
fs.writeFile(filePath, stringToStore, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
