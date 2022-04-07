#!/usr/bin/node

const ilist = require('./100-data').list;
console.log(ilist);
const nlist = ilist.map((elem, index) => elem * index);
console.log(nlist);
