#!/usr/bin/env python3
import math
import sys

#script that takes start and end from command line and prints the range
start = int(sys.argv[1])
end = int(sys.argv[2])

total = end-start+1
#for i in range(total):
#	print(i+start)

for i in range(total):
	if (i+start)%2==1:
		print(i+start)
