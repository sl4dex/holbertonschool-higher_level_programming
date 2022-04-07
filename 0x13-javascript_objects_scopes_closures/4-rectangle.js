#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h, w, row;
    for (h = this.height; h >= 1; h--) {
      for (w = this.width, row = ''; w >= 1; w--) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const auxh = this.height;
    this.height = this.width;
    this.width = auxh;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
