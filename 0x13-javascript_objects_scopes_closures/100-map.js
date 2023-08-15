#!/usr/bin/node

const list = require('./100-data');

console.log(list.list);
console.log(list.list.map((num, index) => num * index));
