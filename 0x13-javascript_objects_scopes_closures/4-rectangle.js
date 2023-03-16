#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
Create an instance method called rotate() that exchanges the width and the height of the rectangle
Create an instance method called double() that multiples the width and the height of the rectangle by 2

*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let symbol = 'X';
    // concatenate X to symbol
    for (let i = 1; i < this.width; i++) {
      symbol += 'X';
    }

    // print concatenated string
	let j = this.height;
	while (j > 0) {
	console.log(symbol);
	j--;


	}

  }

  double () {
  this.height *= 2;
  this.width *= 2;
  }

  rotate () {
  [this.width, this.height] = [this.height, this.width];
  }


};
