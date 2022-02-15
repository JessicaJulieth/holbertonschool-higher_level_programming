#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const dicc = {};
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed) {
        if (dicc[task.userId]) {
          dicc[task.userId]++;
        } else {
          dicc[task.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});
