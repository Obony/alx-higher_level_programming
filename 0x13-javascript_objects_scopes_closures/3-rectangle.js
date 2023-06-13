#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let xRow = '';
      for (let j = 0; j < this.width; j++) {
        xRow += 'X';
      }
      console.log(xRow);
    }
  }
}
module.exports = Rectangle;
