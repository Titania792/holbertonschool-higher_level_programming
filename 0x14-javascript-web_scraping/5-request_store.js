#!/usr/bin/node

const url = process.argv.slice(2)[0];
const file = process.argv.slice(2)[1];

const request = require('request');
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const urlContent = body;
    fs.appendFile(file, urlContent, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
