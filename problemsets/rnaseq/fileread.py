#!/usr/bin/env python3
import sys
import re

file1 = open("Log.final.out", "r")
file2 = open("Log.out","r")


#Find these values:
#filename1 = sys.argv[1]
#filename2 = sys.argv[2]
#files = [file1,file2]


uniqmapped = 0
unmapped = 0
mismatchrate = 0
multimapped = 0
unmapped = 0
gtagSplicenum = 0
gcagSplicenum = 0
atacSplicenum = 0
noncon = 0

for line in file1:
	if r'Uniquely mapped reads %' in line:
		uniqmapped_add = re.search(r"((\d+[.]\d+))",line)
		uniqmapped = uniqmapped + float(uniqmapped_add.group(1))
	elif r'Mismatch rate per base, %' in line:
		mismatchrate_add = re.search(r"((\d+[.]\d+))",line)
		mismatcherate = mismatchrate +float(mismatchrate_add.group(1)) 
	elif r'% of reads mapped to multiple loci' in line:
		multimapped_add = re.search(r"((\d+[.]\d+))",line)
		multimapped = multimapped + float(multimapped_add.group(1))
	elif r'unmapped' in line:
		unmapped_add = re.search(r"((\d+[.]\d+))",line)
		unmapped = unmapped + float(unmapped_add.group(1))
	elif r'Number of splices: GT/AG' in line:
		gtagSplicenum_add = re.search(r"((\d+))",line)
		gtagSplicenum = gtagSplicenum + int(gtagSplicenum_add.group(1))
	elif r'Number of splices: GC/AG' in line:
		gcagSplicenum_add = re.search(r"((\d+))",line)
		gcagSplicenum = gcagSplicenum + int(gcagSplicenum_add.group(1))
	elif r'Number of splices: AT/AC' in line:
		atacSplicenum_add = re.search(r"((\d+))",line)
		atacSplicenum = atacSplicenum + int(atacSplicenum_add.group(1))
	elif r'Number of splices: Non-canonical' in line:
		noncon_add = re.search(r"((\d+))",line)
		noncon = noncon + int(noncon_add.group(1))
#	if r'genomeDir' in line:
#		print(line)

for line in file2:
#	if r'Uniquely mapped reads %' in line:
#		uniqmapped_add = re.search(r"((\d+[.]\d+))",line)
#		uniqmapped = uniqmapped + float(uniqmapped_add.group(1))
#	elif r'Mismatch rate per base, %' in line:
#		mismatchrate_add = re.search(r"((\d+[.]\d+))",line)
#		mismatcherate = mismatchrate +float(mismatchrate_add.group(1)) 
#	elif r'% of reads mapped to multiple loci' in line:
#		multimapped_add = re.search(r"((\d+[.]\d+))",line)
#		multimapped = multimapped + float(multimapped_add.group(1))
	#elif r'unmapped' in line:
	#	unmapped_add = re.search(r"((\d+[.]\d+))",line)
	#	unmapped = unmapped + float(unmapped_add.group(1))
#	elif r'Number of splices: GT/AG' in line:
#		gtagSplicenum_add = re.search(r"((\d+))",line)
#		gtagSplicenum = gtagSplicenum + int(gtagSplicenum_add.group(1))
#	elif r'Number of splices: GC/AG' in line:
#		gcagSplicenum_add = re.search(r"((\d+))",line)
#		gcagSplicenum = gcagSplicenum + int(gcagSplicenum_add.group(1))
#	elif r'Number of splices: AT/AC' in line:
#		atacSplicenum_add = re.search(r"((\d+))",line)
#		atacSplicenum = atacSplicenum + int(atacSplicenum_add.group(1))
#	elif r'Number of splices: Non-canonical' in line:
#		noncon_add = re.search(r"((\d+))",line)
#		noncon = noncon + int(noncon_add.group(1))
	if r'genomeDir' in line:
		genome = re.search("r(genomeDir\s+(\S+))",line)
		print(genome.group(1))

