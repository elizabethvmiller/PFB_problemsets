#!/usr/bin/env python3
import re
import sys

fasta = open("Python_08.fasta", "r")
fastadict = {}
new_sequence ="" 

for line in fasta:
	matchheader = re.findall(r"^>(.+)[^\n]", line)
	matchsequence = re.search(r"^([ATCG]+)[^\n]", line)

	if matchheader:
		header = matchheader[0]
		fastadict[header] = 'placeholder'
	elif matchsequence:
		sequence = matchsequence[0]
		new_sequence = new_sequence + sequence
		fastadict[header] = new_sequence
	else:
		new_sequence = ""
print(fastadict)
	

			
