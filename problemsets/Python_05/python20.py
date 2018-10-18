#!/usr/bin/env python3
#import sys

fav_dict = {'book': 'Call of the Wild', 'color': 'blue', 'animal': 'cat', 'tree': 'oak', 'organism': 'cat'}

for option in fav_dict:
        print(option)
option = input("Pick one of the following favorite things above:")

optionvalue = input("Describe your favorite thing in your chosen category:")
fav_dict[option] = optionvalue

print( "Favorite thing is: ",fav_dict[option])

fav_thing = option

for i in fav_dict:
	value = fav_dict[i]
	print (i,'\t', value)
