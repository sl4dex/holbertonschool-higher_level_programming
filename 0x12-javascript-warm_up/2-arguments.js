#!/usr/bin/node
const arr = process.argv.slice(2);
if (!arr[0]) {
  console.log('No argument');
} else {
  console.log('Argument passed');
}
