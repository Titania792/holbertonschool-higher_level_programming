#!/usr/bin/node

function secondBiggest (list) { // list is the array to be sorted
  if (list.length < 2) { // if the array is empty or has only one element, return 0
    return 0;
  }
  list.sort(function (a, b) { // sort the array in ascending order
    return a - b;
  });
  return list[list.length - 2]; // return the second biggest element
}
console.log(secondBiggest(process.argv.slice(2))); // print the second biggest element of the array
