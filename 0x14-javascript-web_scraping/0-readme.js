#!/usr/bin/node
// Reads and prints the content of a file
const fs = require('fs');
const filepath = process.argv[2];

if (!filepath) {
  console.error('Please provide a filepath');
  process.exit(1);
}

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
