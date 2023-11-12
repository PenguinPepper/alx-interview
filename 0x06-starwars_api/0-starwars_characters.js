#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
*/

const request = require('request');
const movieId = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + movieId, function (error, res, body) {
  if (error) throw error;
  const response = JSON.parse(body);
  for (const character of response.characters) {
    request(character, function (err, ress, bod) {
      const characterBody = JSON.parse(bod);
      console.log(characterBody.name);
      if (err) throw err;
    });
  }
});
