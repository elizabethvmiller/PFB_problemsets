#!/usr/bin/env python3
import sys
import math

list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

it_list = iter(list)
for i in it_list:
	print(len(i),'\t',i)
