#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

const url = process.argv[2];
axios.get(url).then(function (response) {
  // handle success
  fs.writeFile(process.argv[3], response.data, err => {
    if (err) {
      console.error(err);
    }
  });
}).catch(function (error) {
  // handle error
  console.log('code: ' + error.response.status);
});
