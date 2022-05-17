#!/usr/bin/node
const axios = require('axios');

const url = process.argv[2];
axios.get(url).then(function (response) {
  // handle success
  console.log('code: ' + response.status);
}).catch(function (error) {
  // handle error
  console.log('code: ' + error.response.status);
});
