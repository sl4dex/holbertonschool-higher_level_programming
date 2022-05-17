#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv.slice(2);
const content = myArgs[1];

fs.writeFile(myArgs[0], content, err => {
  if (err) {
    console.error(err);
  }
});
