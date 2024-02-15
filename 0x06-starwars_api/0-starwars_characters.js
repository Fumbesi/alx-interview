#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status Code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status Code:', response.statusCode);
        process.exit(1);
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
