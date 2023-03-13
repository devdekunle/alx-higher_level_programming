#!/usr/bin/node
const process = require('process');
let args = parseInt(process.argv[2]);
if (args.length < 3 || isNaN(args)) {
  console.log('Missing size');
} else {
  let sqPrint = 'X';
  for (let i = 0; i < args - 1; i++) {
    sqPrint += 'X';
  }
  while (args > 0) {
    console.log(sqPrint);
    args--;
  }
}
