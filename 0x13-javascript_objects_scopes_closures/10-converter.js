#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return parseInt(number, 10).toString(base);
  };
};
