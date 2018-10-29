#!/usr/bin/env python3
import re
import sys

fasta = open("Python_08.fasta", "r")
fastadict = {}
sequence = ""
header = ""

for line in fasta:
	line = line.rstrip()
	if '>' in line:
		if len(sequence) > 0:
			seq_length = len(sequence)
			fastadict[header] = {}
			fastadict[header]['sequence'] = sequence
			fastadict[header]['seq_length'] = seq_length
			print("ID:{}\tLENGTH:{}\tSEQ:{}".format(header,fastadict[header]['seq_length'],fastadict[header]['sequence']))
		header = line[1:]
		sequence = ""
	else:
		sequence = sequence + line

#need this here to make sure that last entry is ok
if len(sequence) > 0:
	seq_length = len(sequence)
	fastadict[header] = {}
	fastadict[header]['sequence'] = sequence
	fastadict[header]['seq_length'] = seq_length
#print(fastadict)
