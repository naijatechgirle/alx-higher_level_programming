i#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let i = 0;
if (num) {
	while (i < num) {
		console.log('C is fun');
		i++;
	}
} else {
	console.log('Missing number of occurrences')
}
