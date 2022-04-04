#!/usr/bin/node
function add (a, b) {
  if (!a || !b) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
}
const arr = process.argv.slice(2);
console.log(add(arr[0], arr[1]));
