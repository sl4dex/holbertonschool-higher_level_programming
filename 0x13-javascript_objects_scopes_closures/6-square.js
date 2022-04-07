#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (chr = 'X') {
    let h, w, row;
    for (h = this.width; h >= 1; h--) {
      for (w = this.height, row = ''; w >= 1; w--) {
        row += chr;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
