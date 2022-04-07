#!/usr/bin/node
const arr = process.argv.slice(2);
let num = parseInt(arr[0]);
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (num; num >= 1; num--) {
    console.log('C is fun');
  }
}
