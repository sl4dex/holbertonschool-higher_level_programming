#!/usr/bin/node

const axios = require('axios');

const users = {};
const url = process.argv[2];
axios.get(url).then(function (response) {
  // handle success
  const usertask = response.data;
  for (let i = 0; i < usertask.length; i++) {
    if (usertask[i].completed === false) {
      continue;
    }
    if (String(usertask[i].userId) in users) {
      users[String(usertask[i].userId)] += 1;
    } else {
      users[String(usertask[i].userId)] = 1;
    }
  }
  console.log(users);
}).catch(function (error) {
  // handle error
  console.log(error);
});
