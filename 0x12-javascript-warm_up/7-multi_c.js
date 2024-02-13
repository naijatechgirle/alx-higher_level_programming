#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let a = 0;
if (num) {
  while (a < num) {
    console.log('C is fun');
    a++;
  }
} else {
  console.log('Missing number of occurrences');
}
