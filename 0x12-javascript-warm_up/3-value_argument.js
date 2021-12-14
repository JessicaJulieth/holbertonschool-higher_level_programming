#!/usr/bin/node
const myVar = process.argv;
if (myVar.length < 3){
console.log("No argument");
}else {
console.log(myVar[2]);
}
