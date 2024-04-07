#!/usr/bin/node
const arg = process.argv;
if (Number.isInteger(parseInt(arg[2]))) {
  console.log('My number: ' + arg[2]);
} else {
  console.log('Not a number');
}
