#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X

*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      const newObject = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let symbol = 'X';
    // concatenate X to symbol
    for (let i = 0; i < this.width; i++) {
      symbol += 'X';
    }

    // print concatenated string
    while (this.height > 0) {
      console.log(symbol);
      this.height--;
    }
  }
};
