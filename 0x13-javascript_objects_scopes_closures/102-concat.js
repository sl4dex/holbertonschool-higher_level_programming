#!/usr/bin/node
const fs = require('fs');
const fileA = './' + process.argv[2];
const fileB = './' + process.argv[3];
const fileC = './' + process.argv[4];
const dataA = fs.readFileSync(fileB, 'utf-8');
const dataB = fs.readFileSync(fileA, 'utf-8');
fs.writeFile(fileC, dataA + dataB, err => {
  if (err) {
    console.error(err);
  }
});
