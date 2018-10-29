#!/usr/bin/env python3

text = open("Python_06.txt", "r")
newtext = open("copiedPython_06.txt","w")
for line in text:
	line = line.rstrip()
	uppercase = line.upper()
	newtext.write(uppercase+'\n')
text.close()
newtext.close()

