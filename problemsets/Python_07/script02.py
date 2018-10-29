#!/usr/bin/env python3
import re

fo = open("Python_07.fasta","r")
fastasequence = ""
fastadict={}
for line in fo:
	found = re.match(r"^>.+[^\n]", line)
	fastakey = str(found)

	if found ==[]:
		cleanedline = line.rstrip()
		fastasequence = fastasequence + cleanedline
		print(fastasequence)
#		fastadict[fastakey] = fastasequence
#print(fastadict)	

#For problem 4
#	if found!= []:
#		foundin = re.search(r"^>(\S+)\s(.+)",line)
#		identifier = foundin.group(1)
#		description = foundin.group(2)
#		sequence = foundin.group(3)
#		print('id:',identifier)
#		print('desc:',description)
#		print(sequence)
