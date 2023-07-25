#!/usr/bin/node
const args = require('process').argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], { encoding: 'utf8' }, err => {
  if (err) console.log(err);
});
