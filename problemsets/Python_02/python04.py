#!/usr/bin/env python3
import sys
import math

#problem 8 - testing if given number is +/-

value = int(sys.argv[1])#getting the value from command prompt
posneg = int(value)%2 #modulus  0 = positve 1=negative

if value ==0:
	print("value is 0")
elif posneg == 0:
	if value < 50:
		print("it is an even number that is smaller than 50")
	elif value >50 and bool((value%3==0))==True:
		print("it is larger than 50 and divisible by 3")
	else:
		print("positive")
else:
	print("negative")


