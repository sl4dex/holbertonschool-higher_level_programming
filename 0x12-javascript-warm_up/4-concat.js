#!/usr/bin/node
const arr = process.argv.slice(2);
if (!arr[0]) {
  console.log('undefined is undefined');
} else if (arr[0] && arr.length === 1) {
  console.log(arr[0] + ' is undefined');
} else if (arr.length >= 2) {
  console.log(arr[0] + ' is ' + arr[1]);
}
