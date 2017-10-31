file_name = 'rosalind_orf.txt'
dna_file = open(file_name, 'r')
dna_seq = ''
for line in dna_file:
    if line.startswith('>'):
		dna_seq = ''
    else:
        new_line = line.rstrip()
        dna_seq = dna_seq + str(new_line)
dna_file.close()
#dna_seq = raw_input('the DNA sequence')

#transcribe the complementing strand
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
#print dna_rev


#transcribe to RNA
rna_seq = ""
for nucleotide in dna_seq:
	if nucleotide == 'T':
		nucleotide = 'U'
		rna_seq = rna_seq + nucleotide
	else:
		rna_seq = rna_seq + nucleotide
#print rna_seq

#transcribe the complementing strand to RNA
rna_rev = ""
for nucleotide in dna_rev:
	if nucleotide == 'T':
		nucleotide = 'U'
		rna_rev = rna_rev + nucleotide
	else:
		rna_rev = rna_rev + nucleotide
#print rna_rev


#translate the RNA to proteins

#creat a dictionary to define all 64 codons
#the stop codoms have * as the value
codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
              "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
              "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
              "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
              "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
              "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
              "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
              "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
              "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
              "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
              "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
              "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
              "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
              "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
              "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


#loop throuth the codons in DNA

#loop throuth the codons in frame1
codon_list = []
codon_total_num = len(rna_seq)/3
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3
	codon_end = codon_start + 3
	codon = rna_seq[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list
#translate the codon into protein
protein = ''
for codons in codon_list:
	protein = protein + str(codon_table.get(codons))
#looking for valid sequence
for n in range(len(codon_list)):
	if protein[n] == 'M':
		m = protein.find('*',n)
		if m != -1:
			print protein[n:m]
			
			
#loop throuth the codons in frame2
codon_list = []
codon_total_num = (len(rna_seq) - 1)/3
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3 + 1
	codon_end = codon_start + 3
	codon = rna_seq[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list
#translate the codon into protein
protein = ''
for codons in codon_list:
	protein = protein + str(codon_table.get(codons))
#looking for valid sequence
for n in range(len(codon_list)):
	if protein[n] == 'M':
		m = protein.find('*',n)
		if m != -1:
			print protein[n:m]
			
			
#loop throuth the codons in frame3
codon_list = []
codon_total_num = (len(rna_seq) - 2)/3
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3 + 2
	codon_end = codon_start + 3
	codon = rna_seq[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list
#translate the codon into protein
protein = ''
for codons in codon_list:
	protein = protein + str(codon_table.get(codons))
#looking for valid sequence
for n in range(len(codon_list)):
	if protein[n] == 'M':
		m = protein.find('*',n)
		if m != -1:
			print protein[n:m]
			
			
#loop throuth the codons in frame-1
codon_list = []
codon_total_num = len(rna_rev)/3
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3
	codon_end = codon_start + 3
	codon = rna_rev[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list
#translate the codon into protein
protein = ''
for codons in codon_list:
	protein = protein + str(codon_table.get(codons))
#looking for valid sequence
for n in range(len(codon_list)):
	if protein[n] == 'M':
		m = protein.find('*',n)
		if m != -1:
			print protein[n:m]
			
			
#loop throuth the codons in frame-2
codon_list = []
codon_total_num = (len(rna_rev)-1)/3
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3 + 1
	codon_end = codon_start + 3
	codon = rna_rev[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list
#translate the codon into protein
protein = ''
for codons in codon_list:
	protein = protein + str(codon_table.get(codons))
#looking for valid sequence
for n in range(len(codon_list)):
	if protein[n] == 'M':
		m = protein.find('*',n)
		if m != -1:
			print protein[n:m]
			
			
#loop throuth the codons in frame-3
codon_list = []
codon_total_num = (len(rna_rev)-2)/3
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3 + 2
	codon_end = codon_start + 3
	codon = rna_rev[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list
#translate the codon into protein
protein = ''
for codons in codon_list:
	protein = protein + str(codon_table.get(codons))
#looking for valid sequence
for n in range(len(codon_list)):
	if protein[n] == 'M':
		m = protein.find('*',n)
		if m != -1:
			print protein[n:m]
