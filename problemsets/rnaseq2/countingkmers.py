#!/usr/bin/env python3

import re
import sys
from Bio import SeqIO

fastqfile = sys.argv[2]
kmer_length =int(sys.argv[1])
num_see = int(sys.argv[3])

kmerdict = {}

for seq_record in SeqIO.parse(fastqfile, 'fastq'):
	sequence_str = str(seq_record.seq)
	sequence_str = sequence_str.rstrip()
	rounds = len(sequence_str)-kmer_length+1 #Add the +1 bc python doesnt count well

	for i in range(rounds):
		kmer = sequence_str[i:i+kmer_length]
		if kmer in kmerdict:
			kmerdict[kmer] +=1
		else:
			kmerdict[kmer] = 1

kmer_list = kmerdict.items()
kmer_sort = sorted(kmer_list, key=lambda tup: tup[1], reverse=True)

for i in range(num_see):
	print (kmer_sort[i])
