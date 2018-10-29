#!/usr/bin/env python3

import sys

#opening files
allgenes = open("alpaca_all_genes.tsv","r")
stemcell = open("alpaca_stemcellproliferation_genes.tsv","r")
pigments = open("alpaca_pigmentation_genes.tsv","r")

#writing files
gene_manip = open("alpaca_manipulations.txt","w")

#generating sets
setAll = set()
setStem = set()
setPigm = set()

for line in allgenes:
	if 'Gene' in line:
		continue
	line = line.rstrip()
	setAll.add(line)

for line in stemcell:
	if 'Gene' in line:
		continue
	line = line.rstrip()
	setStem.add(line)

for line in pigments:
	if 'Gene' in line:
		continue
	line = line.rstrip()
	setPigm.add(line)

gene_manip.write(str(setAll)+'\n')
gene_manip.write(str(setStem)+'\n')
gene_manip.write(str(setPigm)+'\n')

allgenes.close()
stemcell.close()
pigments.close()

print("wrote to file 'alpaca_manipulations.txt'")
