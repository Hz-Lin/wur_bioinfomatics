dna_seq = raw_input('what is the DNA sequence')
rna_seq = ""
for nucleotide in dna_seq:
	if nucleotide == 'T':
		nucleotide = 'U'
		rna_seq = rna_seq + nucleotide
	else:
		rna_seq = rna_seq + nucleotide
print rna_seq