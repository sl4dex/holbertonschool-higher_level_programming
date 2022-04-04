#!/usr/bin/node
const a = process.argv;
if (!a[2]) {
  console.log('No argument');
} else if (a[2] && !a[3]) {
  console.log('Argument passed');
} else if (a[2] && a[3]) {
  console.log('Arguments passed');
}
