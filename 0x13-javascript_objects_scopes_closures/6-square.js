#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += c;
    } for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
}

module.exports = Square;
