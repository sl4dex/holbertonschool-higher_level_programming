#!/usr/bin/node
const arr = process.argv.slice(2);
const num = parseInt(arr[0]);
if (!num) {
  console.log('Not a number');
} else {
  console.log(num);
}
