#!/usr/bin/env python3
import sys
import math

#find the start position of an EcoRI site (G/AATTC) in a given DNA sequence

dna = sys.argv[1]
dnacase = dna.upper()

pythonstart = dnacase.find("GAATTC")
ecoRIstart = pythonstart+1
ecoRIend = pythonstart + 6

message = "In the given 5'->3' DNA sequence, the first EcoRI site begins at nucleotide {} and ends at nucleotide {}."

new_message = message.format(ecoRIstart, ecoRIend)
print (new_message)
