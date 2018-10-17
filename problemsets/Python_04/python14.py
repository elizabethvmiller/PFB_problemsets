#!/usr/bin/env python3
import sys
import math

list = [101,2,15,22,95,33,2,27,72,15,52]

#it_list = iter(list)
#for i in it_list:
#	if i%2 == 0:
#		print(i)

sortedlist = sorted(list)
it_list2 = iter(sortedlist)
evensum = 0
oddsum = 0
for i in it_list2:
#	print (i)
	if i%2 == 0:
		evensum = i + evensum
	else:
		oddsum = i + oddsum
print("Sum of even numbers:",evensum)
print("Sum of odd numbers:",oddsum) 

