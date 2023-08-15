#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((!w || w < 0) || (!h || h < 0)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
}

module.exports = Rectangle;
