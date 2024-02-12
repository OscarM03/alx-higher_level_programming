#!/usr/bin/node
const myArray = process.argv;
let myValue;

if (myArray[2]) {
  myValue = parseInt(myArray[2], 10);
}

if (isNaN(myValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ', myValue);
}
