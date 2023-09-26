#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    const characters = json.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const json = JSON.parse(body);
          console.log(json.name);
        }
      });
    }
  }
});
