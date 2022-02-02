#!/usr/bin/node

const movieID = process.argv[2];
const request = require('request');
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const X = JSON.parse(body);
    console.log(X.title);
  }
});
