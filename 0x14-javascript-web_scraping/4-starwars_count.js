#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
    console.error('Please provide an API URL');
    process.exit(1);
}

const characterId = '18';

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const count = JSON.parse(body).count;
        console.log(count);
    }
})
