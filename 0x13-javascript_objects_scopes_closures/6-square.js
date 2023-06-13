#!/usr/bin/node
class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let xRow = '';
      for (let j = 0; j < this.width; j++) {
        xRow += c;
      }
      console.log(xRow);
    }
  }
}
module.exports = Square;
