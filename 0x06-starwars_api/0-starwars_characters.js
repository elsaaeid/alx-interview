#!/usr/bin/node
/**
 * Entry point - makes requests to Star Wars API
 * for movie info based movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 * in order of appearance in the initial response.
 */


const request = require('request-promise');
const movieId = process.argv[2];


async function getMovieCharacters(movieId) {
  try {
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    const movieData = await request(movieUrl, { json: true });
    const characters = movieData.characters;

    for (const characterUrl of characters) {
      const characterData = await request(characterUrl, { json: true });
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}
getMovieCharacters(movieId);
