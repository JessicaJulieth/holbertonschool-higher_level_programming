#!/usr/bin/node

const myVar = process.argv[2];
if (myVar === undefined || Number.isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= myVar; i++) {
    console.log('x'.repeat(myVar));
  }
}
