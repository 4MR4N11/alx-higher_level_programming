#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    let char = 'X';
    if (c) {
      char = char.replace('X', 'C');
    }
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += char;
    } for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
}

module.exports = Square;
