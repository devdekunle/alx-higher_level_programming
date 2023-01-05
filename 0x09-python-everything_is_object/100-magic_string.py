#!/usr/bin/python3
def magic_string(var={"num": 0}):
   var["num"] += 1
   return str("BestSchool, " * var["num"])[:-2]
