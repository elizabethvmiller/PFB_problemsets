#!/usr/bin/env python3

original = open("Python_06.seq.txt", "r")
fastafile = open("Python_06.seqRC.fasta","w")

for line in original:
	line = line.rstrip()
	gene,sequence = line.split()
	uppercaseDNA = sequence.upper()

	#converstion of A-T
	temporaryA = uppercaseDNA.replace("A", "x")
	temporaryT = temporaryA.replace("T", "A")
	replacedAT = temporaryT.replace("x", "T")

	#conversion of G-C
	temporaryC = replacedAT.replace("C","y")
	temporaryG = temporaryC.replace("G","C")
	complement35 = temporaryG.replace("y","G")

	complement53 = complement35[::-1]
	
	print('>RC_'+gene+'\n'+complement53)
