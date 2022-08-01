#!/usr/bin/node
const str = 'X';
const i = process.argv[2];

for (let j = 0; j < i; j++) {
  console.log(str.repeat(i));
}
