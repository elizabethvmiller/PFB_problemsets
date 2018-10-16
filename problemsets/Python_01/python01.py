#!/usr/bin/env python3
import sys

#first exercise in python extracting values from command line
name = sys.argv[1] #get name from first position
fvcolor = sys.argv[2] #get favorite color from second position
fvactivity = sys.argv[3] #get favorite activity from thrid position
fvanimal = sys.argv[4] #get favorite animal from fourth position
# using comma keeps it indented, using + makes it justified with above
print ("My name :", name, "\n"+
      "My favorite color :", fvcolor, "\n"+
      "My favorite activity :", fvactivity, "\n"+
      "My favorite animal :", fvanimal)
