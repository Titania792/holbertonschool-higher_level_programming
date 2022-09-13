#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
fs.writeFile(argv.slice(2)[0], argv.slice(2)[1], err => {
  if (err) {
    console.error(err);
  }
});
