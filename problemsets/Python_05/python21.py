#!/usr/bin/env python3
import sys

setA = {3,14,15,9,26,5,35,9}
setB = {60,22,14,0,9}

intersection = setA&setB
difference = setA-setB
union = setA|setB
symdifference = setA^setB

print("Intersection is:", intersection)
print("Difference is:", difference)
print("Union is:", union)
print("Symmetrical difference is:", symdifference)
