#!/usr/bin/env python3

from Bio import SeqIO

for seq_rec in SeqIO.parse('four_reads.fastq','fastq'):
	print(seq_rec.qual)
