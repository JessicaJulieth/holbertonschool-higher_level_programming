#!/usr/bin/node
const myVar = (process.argv);
const x = parseInt(myVar[2]);
if (myVar[2] === NaN) 
{
  console.log("Not a number");
}
    else 
    {
        console.log("My number: " + x);
    }
