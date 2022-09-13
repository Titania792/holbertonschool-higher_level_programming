#!/usr/bin/node

const axios = require('axios').default;
const id = process.argv.slice(2)[0];
axios.get('https://swapi-api.hbtn.io/api/films/' + id)
  .then(function (response) {
    console.log(response.data.title);
  });