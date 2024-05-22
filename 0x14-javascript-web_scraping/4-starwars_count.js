#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;

  data.results.forEach((film) => {
    if (
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`
      )
    ) {
      count++;
    }
  });

  console.log(count);
});
