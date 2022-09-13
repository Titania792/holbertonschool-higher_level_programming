#!/usr/bin/node

const url = process.argv.slice(2)[0];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let x = 0;
    let moviesID = 0;
    const urlJSON = JSON.parse(body);
    while (urlJSON.results[x]) {
      let y = 0;
      const chars = urlJSON.results[x].characters;
      while (chars[y]) {
        if (chars[y].includes('/18/')) {
          moviesID++;
        }
        y++;
      }
      x++;
    }
    console.log(moviesID);
  }
});
