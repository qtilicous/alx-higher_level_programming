#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesURL = 'https://swapi-api.alx-tools.com/api/people/18/';

  const count = films.reduce((acc, film) => {
    if (film.characters.includes(wedgeAntillesURL)) {
      return acc + 1;
    }
    return acc;
  }, 0);

  console.log(count);
});
