#!/usr/bin/node

const file = process.argv.slice(2)[0];
const fs = require('fs');
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
