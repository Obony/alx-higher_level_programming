#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    if (!this.width || !this.height) {
      return;
    }

    let x = c;
    for (let i = 1; i < this.width; i++) {
      x += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }
}

module.exports = Square;
