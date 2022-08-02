#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) { // This function increments the number and calls the function
  return theFunction(number + 1);
};
