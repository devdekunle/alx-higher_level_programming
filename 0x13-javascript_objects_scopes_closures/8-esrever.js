#!/usr/bin/node
/*
Write a function that returns the reversed version of a list:

Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/

exports.esrever = function (list) {
  if (list === undefined) {
    return null;
  } else {
    const reversedList = [];
    let lastElement = list.length - 1;
    let i = 0;
    while (lastElement >= 0) {
      reversedList[i] = list[lastElement];
      --lastElement;
      ++i;
    }
    return reversedList;
  }
};
