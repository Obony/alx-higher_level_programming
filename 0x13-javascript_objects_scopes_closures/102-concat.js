#!/usr/bin/node
const fs = require('fs');
const a = process.argv[2];
const b = process.argv[3];
const c = process.argv[4];
fs.readFile(a, 'utf-8', function (err, data) {
  if (err) throw err;
  fs.writeFile(c, data, function (err) { if (err) throw err; });
});
fs.readFile(b, 'utf-8', function (err, data) {
  if (err) throw err;
  fs.appendFile(c, data, function (err) { if (err) throw err; });
});
