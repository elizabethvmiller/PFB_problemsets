#!/usr/bin/env python3

fo = open("Python_06.fastq", "r")
totline = 0
totchar = 0
for line in fo:
	totline = totline + 1
	line = line.rstrip()
	totchar = totchar + len(line)
avelen = totchar/totline
print(totline)
print(totchar)
print(avelen)

