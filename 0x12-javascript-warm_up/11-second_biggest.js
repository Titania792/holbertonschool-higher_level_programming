#!/usr/bin/node

function secondBiggest (list) { // list is the array to be sorted
  if (list.length < 2) { // if the array is empty or has only one element, return 0
    return 0;
  }
  let biggest = 0;
  let secondBiggest = 0;
  for (let i = 0; i < list.length; i++) { // loop through the array
    if (list[i] > biggest) { // if the current element is bigger than the biggest element, set the biggest element to the current element
      secondBiggest = biggest;
      biggest = list[i];
    } else if (list[i] > secondBiggest) { // if the current element is bigger than the second biggest element, set the second biggest element to the current element
      secondBiggest = list[i];
    }
  }
  return secondBiggest;
}
console.log(secondBiggest(process.argv.slice(2))); // print the second biggest element of the array passed in as an argument, slice the array to remove the first element (the script name)
