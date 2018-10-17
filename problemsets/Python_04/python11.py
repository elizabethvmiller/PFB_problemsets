#!/usr/bin/env python3
import sys
import math

#script that splits a string into a list and sorts in various ways
string = "sapiens, erectus, neanderthalensis"
print (string)

convertedstring = string.split(",")
print (convertedstring)

sortedlist = sorted(convertedstring)
print(sortedlist)

sortedlength = sorted(sortedlist, key=len)
print(sortedlength)
