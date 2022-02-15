#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dicc = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed && dicc[task.userId]) {
          dicc[task.userId]++;
        } else if (!dicc[task.userId] && task.completed) {
          dicc[task.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});
