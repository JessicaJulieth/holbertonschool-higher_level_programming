#!/usr/bin/node
const myVar = process.argv[2];
if (myVar != isNaN) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= myVar; i++) {
    console.log('C is fun');
  }
}
