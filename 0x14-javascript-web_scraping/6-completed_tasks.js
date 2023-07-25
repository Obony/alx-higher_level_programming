#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

const completedTasks = {};
const url = String(args[2]);
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  body = JSON.parse(body);
  for (const task of body) {
    if (task.completed) {
      if (task.userId in completedTasks) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
