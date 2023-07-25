#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + String(args[2]);
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
