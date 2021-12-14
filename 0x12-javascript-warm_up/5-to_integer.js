#!/usr/bin/node
const myVar = Number.parseInt(process.argv);
if (myVar[2] === parseInt(myVar[2])) {
console.log("My number:" + parseInt(myVar[2]));
}else {
console.log("Not a number");
}
