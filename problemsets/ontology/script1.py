#!/usr/bin/env python3
import pronto

ont = pronto.Ontology('go.owl')
iterm_obj = ont['GO:0006355']
term_name = term_obj.name
count = 0
for term in ont:
	if term.children:
		print(term)
		count +=1
print(count):w

