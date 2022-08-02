#!/usr/bin/node

const fs = require('fs'); // the file system module is used to read the files and write the result to the destination file
fs.writeFileSync(process.argv[4], fs.readFileSync(process.argv[2], 'utf-8') + fs.readFileSync(process.argv[3], 'utf-8'));
/*  The writeFileSync method is used to write the result to the destination file
    The readFileSync method is used to read the source files
    The utf-8 encoding is used to read the files as strings */
