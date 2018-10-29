#!/usr/bin/env python3

class DNASequence(object):
	#Part 1
	#class attributes
	def __init__(self, sequence, name, organism):
		self.sequence = sequence
		self.name = name
		self.organism = organism

	#Part 4
	#methods
	def getSeqLength(self):
		return len(str(self.sequence))
	
	#Part 5
	def getNucComp(self):
		sequence = str(self.sequence)
		compA = sequence.count('A')/len(sequence)
		formA = '{:.2%}'.format(compA)

		compT = sequence.count('T')/len(sequence)
		formT = '{:.2%}'.format(compT)

		compC = sequence.count('C')/len(sequence)
		formC = '{:.2%}'.format(compC)

		compG = sequence.count('G')/len(sequence)
		formG = '{:.2%}'.format(compG)
		
		composition = "A:{},T:{}, C:{},G:{}".format(formA, formT, formC, formG)
		return composition

	#Part 6
	def getGCcontent(self):
		sequence = str(self.sequence)
		GCcontent = (sequence.count('C')+sequence.count('G'))/len(sequence)
		return GCcontent

#Part 2 incorporated into part 3

#Part 3	
dna_rec_ob1 = DNASequence('ATGATGATGATG', 'TEST', 'CAT')
dna_rec_ob2 = DNASequence('TAGTAGTAGTAG', 'TEST2', 'DOG')

for i in [dna_rec_ob1, dna_rec_ob2]:
	print('name:' , i.name, ' ', 'organism:' , i.organism, ' ','seqlength:', ' ', i.getSeqLength(), 'sequence:' , i.sequence, i.getNucComp(), 'GC content:', i.getGCcontent())
