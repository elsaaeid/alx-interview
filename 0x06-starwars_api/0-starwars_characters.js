#!/usr/bin/node
/**
 * Entry point - makes requests to Star Wars API
 * for movie info based movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 */
const util = require('util');
const request = util.promisify(require('request'));
const movieId = process.argv[2];
if (!movieId || isNaN(movieId)) {
  process.exit(1);
}

async function getMovieCharacters (movieId) {
  try {
    const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
    let movieData = await (await request(movieUrl)).body;
    movieData = JSON.parse(movieData);
    const characters = movieData.characters;

    for (let i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      let character = await (await request(urlCharacter)).body;
      character = JSON.parse(character);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

getMovieCharacters(movieId);
