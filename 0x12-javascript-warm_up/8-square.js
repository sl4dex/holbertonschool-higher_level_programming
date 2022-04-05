#!/usr/bin/node
const arr = process.argv.slice(2);
const num = parseInt(arr[0]);
let h, w, row;
if (!num) {
  console.log('Missing size');
} else {
  for (h = num; h >= 1; h--) {
    for (w = num, row = ''; w >= 1; w--) {
      row += 'X';
    }
    console.log(row);
  }
}
