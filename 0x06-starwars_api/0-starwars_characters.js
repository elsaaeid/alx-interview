#!/usr/bin/node
/**
 * Entry point - makes requests to Star Wars API
 * for movie info based movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 * in order of appearance in the initial response.
 */

const util = require('util');
const request = util.promisify(require('request'));
const movieId = process.argv[2];

async function getMovieCharacters (movieId) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  let response = await (await request(movieUrl)).body;
  movieData = JSON.parse(response);
  const characters = movieData.characters;

  for (const characterUrl of characters) {
    const characterData = await request(characterUrl, { json: true });
    console.log(characterData.name);
  }
}

getMovieCharacters(movieId);
