#!/usr/bin/node

const myVar = (process.argv);
if (myVar.length < 2) {
  console.log('0');
} else if (myVar.length <= 3) {
  console.log('0');
} else {
  myVar.sort(function (a, b) {
    return b - a;
  });

  console.log(myVar[3]);
}
