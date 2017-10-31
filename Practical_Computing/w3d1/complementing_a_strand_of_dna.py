dna_seq = raw_input('what is the DNA sequence')
dna_comp = ''
for nutide in dna_seq:
	if nutide == 'T':
		new_nutide = 'A'
	elif nutide == 'A':
		new_nutide = 'T'
	elif nutide == 'C':
		new_nutide = 'G'
	else:
		new_nutide = 'C'	
	dna_comp = dna_comp + new_nutide	
dna_rev = dna_comp[::-1]
print dna_rev