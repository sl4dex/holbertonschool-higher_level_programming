#!/usr/bin/node
const axios = require('axios');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios.get(url).then(function (response) {
  // handle success
  console.log(response.data.title);
}).catch(function (error) {
  // handle error
  console.log('code: ' + error.response.status);
});
