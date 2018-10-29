#!/usr/bin/env python3

import sys
import re

dictsam = {}
count = 0
samfile = open("bowtie2.sam", "r")
for line in samfile:
	found = re.search(r'(\S+)\s+\d+\s+(\S+)[\^]',line)
	read = found.group(1)
	gene = found.group(2)
	
	dictsam[gene]={}
	print(dictsam)
	dictsam[gene]['reads'] = []
	dictsam[gene]['reads'] =  
	dictsam[gene]['count'] = 0
	
	if gene in dictsam: 
		if read not in dictsam[gene]['reads']:
			print('test')
	else:
		print('no')
#print(dictsam)

	count +=1

	if  count ==5:
		break
	
