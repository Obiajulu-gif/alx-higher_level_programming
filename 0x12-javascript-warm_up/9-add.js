#!/usr/bin/node
const intArray = process.argv;
if (intArray < 3) {
  console.log(NaN);
} else {
  const result = parseInt(intArray[2]) + parseInt(intArray[3]);
  console.log(result);
}
