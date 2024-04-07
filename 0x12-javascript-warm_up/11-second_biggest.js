#!/usr/bin/node
const intArray = process.argv.splice(2);

let biggest = 0;
let secondBiggest = 0;

if (intArray.length <= 1) {
  console.log(0);
} else {
  intArray.forEach(element => {
    const num = parseInt(element);
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest) {
      secondBiggest = num;
    }
  });
  console.log(secondBiggest);
}
