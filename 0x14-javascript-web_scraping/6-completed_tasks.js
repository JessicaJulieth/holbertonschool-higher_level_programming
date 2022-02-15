#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const dicc = {};
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed === true) {
        if (dicc[task.userId] === undefined) {
          dicc[task.userId] = 1;
        } else {
          dicc[task.userId] += 1;
        }
      }
    }
    console.log(dicc);
  }
});
