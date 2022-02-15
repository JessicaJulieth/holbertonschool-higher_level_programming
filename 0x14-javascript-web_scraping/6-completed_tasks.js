#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dicc = {};

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed && dicc[task.userId]) {
          dicc[task.userId] += 1;
        } else if (!dicc[task.userId] && task.completed) {
          dicc[task.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});
