#!/usr/bin/node
const axios = require('axios');

const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
let counter = 0;
axios.get(url).then(function (response) {
  // handle success
  const movies = response.data.results;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.includes(wedge)) {
      counter += 1;
    }
  }
  console.log(counter);
})
  .catch(function (error) {
    console.log(error);
  });
