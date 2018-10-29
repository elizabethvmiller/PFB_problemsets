#!/usr/bin/env python3

from Bio import SeqIO
fastadict = {}

for seq_record in SeqIO.parse('test.fasta', 'fasta'):
	header_str = str(seq_record.id)
	sequence_str = str(seq_record.seq)
	ntA = sequence_str.count('A')
	ntT = sequence_str.count('T')
	ntC = sequence_str.count('C')
	ntG = sequence_str.count('G')

	fastadict[header_str] = {}
	fastadict[header_str]['sequence'] = sequence_str
	fastadict[header_str]['nt_cont'] = {}
	fastadict[header_str]['nt_cont']['A'] = ntA
	fastadict[header_str]['nt_cont']['T'] = ntT
	fastadict[header_str]['nt_cont']['C'] = ntC
	fastadict[header_str]['nt_cont']['G'] = ntG

	conGC = (ntC + ntG)/len(sequence_str)
	gc_con = ("{:.2%}".format(conGC))
	print("The GC% of {} is {}".format(header_str,gc_con))	
