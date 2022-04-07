#!/usr/bin/node
function factorial (num) {
  if (!num) {
    return 1;
  }
  if (num < 0) {
    return;
  }
  return factorial(num - 1) * num;
}
const arr = process.argv.slice(2);
console.log(factorial(parseInt(arr[0])));
