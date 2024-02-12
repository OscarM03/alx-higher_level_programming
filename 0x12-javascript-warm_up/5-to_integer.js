#!/usr/bin/node
const [, , firstArg] = process.argv;

let myValue = parseInt(firstArg, 10);

if (!isNaN(myValue)) {
  console.log('My number: ', myValue);
} else {
  console.log('Not a number');
}
