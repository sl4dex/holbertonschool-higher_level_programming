#!/usr/bin/node
const idict = require('./101-data').dict;
const ndict = {};
for (const key in idict) {
  if (!(ndict[idict[key]])) {
    ndict[idict[key]] = [key];
  } else {
    ndict[idict[key]].push(key);
  }
}
console.log(ndict);
// omg it works
