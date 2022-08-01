#!/usr/bin/node
const args = process.argv; // Array of arguments
const a = ' is ';
const empty = '';

console.log(empty.concat(args[2], a, args[3])); // Concatenate the first and second argument
