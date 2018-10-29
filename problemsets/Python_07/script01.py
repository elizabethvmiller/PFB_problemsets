#!/usr/bin/env python3
import re
import sys

fo = open("Python_07_nobody.txt","r")
for line in fo:
	found = re.search(r"Nobody",line)
#	print(found)

fo = open("Python_07_nobody.txt","r")
for line in fo:
	person = re.sub(r"Nobody",r"Soeren",line)
	print(person)
