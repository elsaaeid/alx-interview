#!/usr/bin/node
/**
 * Entry point - makes requests to Star Wars API
 * for movie info based movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 */
const util = require('util');
const request = util.promisify(require('request'));
const movieId = process.argv[2];

async function getMovieCharacters (movieId) {
  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
  let response = await (await request(movieUrl)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

getMovieCharacters(movieId);
