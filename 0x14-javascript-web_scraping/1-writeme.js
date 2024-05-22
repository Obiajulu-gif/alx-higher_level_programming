#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Please provide a filepath and content');
  process.exit(1);
}

fs.writeFile(filepath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
