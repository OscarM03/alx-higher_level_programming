#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(character => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const info = JSON.parse(body);
      const name = info.name;
      console.log(name);
    });
  });
});
