#!/usr/bin/node

const axios = require('axios');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
axios.get(url).then(function (response) {
  // handle success
  const chars = response.data.characters;
  // for each char film
  for (let i = 0; i < chars.length; i++) {
    axios.get(chars[i]).then(function (respchar) {
      console.log(respchar.data.name);
    }).catch(function (error) {
      // handle error
      console.log(error);
    });
  }
}).catch(function (error) {
  // handle error
  console.log(error);
});
