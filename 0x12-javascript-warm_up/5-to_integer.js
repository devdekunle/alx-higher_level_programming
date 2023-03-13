#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (!isNaN(args[2])) {
  console.log(`My number: ${Math.floor(args[2])}`)
} else {
  console.log('Not a number')
}
