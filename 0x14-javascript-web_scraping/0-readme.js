#!/usr/bin/env node
// Read and print the content of a file in node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
