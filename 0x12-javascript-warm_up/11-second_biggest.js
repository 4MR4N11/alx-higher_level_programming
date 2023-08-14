#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const size = args.length;

if (size === 0 || size === 1) {
  console.log('0');
} else {
  let n = 1;
  const tmp = {
    1: args.slice()
  };
  while (true) {
    let min = Math.min(...tmp[n]);
    if (tmp[n].length === 2) {
      break;
    }
    tmp[n + 1] = tmp[n].filter((number) => {
      return (number !== min) || (number === min && (min = NaN));
    });
    n++;
  }
  console.log(Math.min(...tmp[n]));
}
