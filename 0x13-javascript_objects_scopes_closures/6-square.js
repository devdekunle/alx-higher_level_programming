#!/usr/bin/node
/*
Write a class Square that defines a square and inherits from Square of 5-square.js:

You must use the class notation for defining your class and extends
Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X

*/
// imports the Square module
const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let symbol = c;
      for (let i = 1; i < this.height; i++) {
        symbol += c;
      }
      while (this.height > 0) {
        console.log(symbol);
        this.height--;
      }
    }
  }
};
