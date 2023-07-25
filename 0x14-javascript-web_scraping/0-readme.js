#!/usr/bin/node
const args = require('process').argv;
const fs = require('fs');

if (args[2]) {
  fs.readFile(args[2], 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
