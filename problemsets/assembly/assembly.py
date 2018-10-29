#!/usr/bin/env python3

assembly_file = open("ecoliPB-filtered_0.50.contigs.fasta", "r")
fastadict = {}
sequence = ""
header = ""
lengthlist = []

for line in assembly_file:
	line = line.rstrip()
	if '>' in line:
		if len(sequence) > 0:
			seq_length = len(sequence)
			fastadict[header] = {}
			fastadict[header]['sequence'] = sequence
			fastadict[header]['seq_length'] = seq_length
			lengthlist.append(seq_length)

#			print("ID:{}\tLENGTH:{}\tSEQ:{}".format(header,fastadict[header]['seq_length'],fastadict[header]['sequence']))
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
	lengthlist.append(seq_length)


#Calculate N50
sortedlist = sorted(lengthlist,reverse=True)
genomesize = sum(sortedlist)
calculateN50 = 0
compareN = 0.5*genomesize
n50 = 0
list_L50 = []

for i in range(len(sortedlist)):
	calculateN50 = sortedlist[i] + calculateN50
	list_L50.append(sortedlist[i])
	if calculateN50 > compareN:
		n50 = sortedlist[i]
		break

keycount = len(fastadict.keys())
print("Total number of contigs:",keycount)
print("Min length of contigs:",min(lengthlist))
print("Max length of contigs:",max(lengthlist))
print("N50 for genome size of",genomesize,"bp:",n50)
print("L50 for assembly:", len(list_L50))
