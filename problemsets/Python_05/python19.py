#!/usr/bin/env python3
import sys

fav_dict = {'book': 'Call of the Wild', 'color': 'blue', 'animal': 'cat', 'tree': 'oak', 'organism': 'cat'}

for option in fav_dict:
	print(option)

option = input("Type on of the options listed above:")  
print( "Favorite thing is: ",fav_dict[option] )

