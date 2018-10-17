#!/usr/bin/env python3
import sys
import math

#Problem 9 AT and GC content in a string

#take sequence and convert to same case
dna = sys.argv[1]
lowerdna = dna.lower()

countAT = lowerdna.count("a")+ lowerdna.count("t")
countGC = lowerdna.count("g")+ lowerdna.count("c")
totalDNA = len(lowerdna)

percentAT = (countAT/totalDNA)*100
percentGC = (countGC/totalDNA)*100

print ("AT% in sequence:", percentAT)
print ("GC% in sequence:", percentGC)
