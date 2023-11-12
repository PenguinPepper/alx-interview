#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
*/

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);
const movieId = process.argv[2];

async function movieCharacter () {
  try {
    const response = await requestPromise('https://swapi-api.alx-tools.com/api/films/' + movieId);
    const responseParse = JSON.parse(response.body);
    for (const character of responseParse.characters) {
      const characterResponse = await requestPromise(character);
      const characterResponseParse = JSON.parse(characterResponse.body);
      console.log(characterResponseParse.name);
    }
  } catch (error) {
    console.error(error);
  }
}

movieCharacter();
