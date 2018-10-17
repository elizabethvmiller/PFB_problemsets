#!/usr/bin/env python3
import sys
import math

#given sequence, prints sequence, complement, and reverse complement

dna = sys.argv[1]

#original sequence
uppercaseDNA = dna.upper()

#converstion of A-T
temporaryA = uppercaseDNA.replace("A", "x")
temporaryT = temporaryA.replace("T", "A")
replacedAT = temporaryT.replace("x", "T")

#conversion of G-C
temporaryC = replacedAT.replace("C","y")
temporaryG = temporaryC.replace("G","C")
complement35 = temporaryG.replace("y","G")

complement53 = complement35[::-1]

print("Original sequence:", uppercaseDNA)
print("Complement:", complement35)
print("Reverse Complement:", complement53)
