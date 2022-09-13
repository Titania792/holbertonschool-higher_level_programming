#!/usr/bin/node

const url = process.argv.slice(2)[0];
const request = require('request');
request(url, (err, res) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
