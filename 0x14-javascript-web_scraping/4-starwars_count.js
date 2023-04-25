#!/usr/bin/node
/* prints the number of movies where the
character "Wedge Antilles" is present. */
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  // make body of reponse parsed in json format to make it printable
  const json = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < json.results.length; i++) {
    for (let j = 0; j < json.results[i].characters.length; j++) {
      const charId = json.results[i].characters[j].split('/')[5];
      if (charId === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
