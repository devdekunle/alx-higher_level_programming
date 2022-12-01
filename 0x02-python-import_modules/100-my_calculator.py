#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, div, sub

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("usage: ./calculator.py <a> <operator> <b>")
        exit(1)
    math_operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if math_operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif math_operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif math_operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif math_operator == "*":
        print("{} + {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, *, - and /")
        exit(1)
