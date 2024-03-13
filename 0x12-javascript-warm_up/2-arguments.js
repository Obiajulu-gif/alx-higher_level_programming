#!/usr/bin/node
const args = process.argv.slice(2);

const numArgs = args.lenght;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
