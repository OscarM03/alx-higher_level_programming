#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let charFilms = 0;

  for (let i = 0; i < films.length; i++) {
    const film = films[i];

    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      charFilms++;
    }
  }

  console.log(charFilms);
});
