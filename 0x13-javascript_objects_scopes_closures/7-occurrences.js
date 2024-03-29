#!/usr/bin/node
/*
Write a function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)

*/
exports.nbOccurences = function (list, searchElement) {
  if (list === undefined || searchElement === undefined) {
    return 0;
  } else {
    let count = 0;
    for (let i = 0; i < list.length; i++) {
      if (searchElement === list[i]) {
        ++count;
      }
    }
    return count;
  }
};
