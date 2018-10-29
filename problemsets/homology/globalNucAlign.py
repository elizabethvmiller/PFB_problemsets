#!/usr/bin/env python3
import sys
import re

seq1 = sys.argv[1]
seq2 = sys.argv[2]
match_val = int(sys.argv[3])
mismatch_val = int(sys.argv[4])

align_sum = 0
for i in range(len(seq1)):
	if seq1[i] == seq2[i]:
		align_sum = align_sum + match_val
	else:
		align_sum = align_sum + mismatch_val
print(align_sum)

