#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let char = 'X';
    if (c) {
      char = char.replace('X', 'C');
    }
    let line = '';
    for (let i = 0; i < this.size; i++) {
      line += char;
    }
    for (let j = 0; j < this.size; j++) {
      console.log(line);
    }
  }
}

module.exports = Square;
