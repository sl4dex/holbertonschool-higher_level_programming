#!/usr/bin/node
let arr = process.argv.slice(2);
if (arr.length <= 1) {
  console.log(0);
} else {
  arr = arr.map(x => parseInt(x));
  console.log(arr.sort()[arr.length - 2]);
}
