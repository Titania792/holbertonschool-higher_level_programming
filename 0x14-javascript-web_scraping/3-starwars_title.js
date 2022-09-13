#!/usr/bin/node

const axios = 'https://swapi-api.hbtn.io/api/films/' + id;
const id = process.argv.slice(2)[0];
const request = require('request');
request(axios, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
