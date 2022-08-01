#!/usr/bin/node

function add (a, b) {
  const result = Number(a) + Number(b);
  return result;
}

console.log(add(process.argv[2], process.argv[3]));
