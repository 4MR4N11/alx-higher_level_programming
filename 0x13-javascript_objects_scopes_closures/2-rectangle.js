#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((!w || w < 0) || (!h || h < 0)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
