#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');

request(requestURL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
