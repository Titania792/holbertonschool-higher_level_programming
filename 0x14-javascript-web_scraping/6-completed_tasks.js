#!/usr/bin/node

const url = process.argv.slice(2)[0];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dictO = {};
    const urlContent = JSON.parse(body);
    for (const x in urlContent) {
      if (urlContent[x].completed === true) {
        if (dictO[urlContent[x].userId] == null) {
          dictO[urlContent[x].userId] = 1;
        } else {
          dictO[urlContent[x].userId]++;
        }
      }
    }
    console.log(dictO);
  }
});
