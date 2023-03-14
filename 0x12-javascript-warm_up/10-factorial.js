#!/usr/bin/node
function factorial (n) {
  if (n <= 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const value = parseInt(process.argv[2]);
if (isNaN(value)) {
  console.log(1);
} else {
  console.log(factorial(value));
}
