#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
  const x = JSON.parse(body);
  let count = 0;
  for (const y of x.results) {
    for (const character of y.characters) {
      if (character.search('/18/') > 0) {
        count++;
       }
     }
   }
   console.log(count);
 } 
});
