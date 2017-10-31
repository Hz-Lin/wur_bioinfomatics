# task1 counting DNA nucleotides

dna_seq = raw_input('what is the sequence')
num_a = dna_seq.count('A')
num_c = dna_seq.count('C')
num_g = dna_seq.count('G')
num_t = dna_seq.count('T')
print num_a, num_c, num_g, num_t


#task2 transcribing DNA into RNA

dna_seq = raw_input('what is the DNA sequence')
rna_seq = ""
for nucleotide in dna_seq:
	if nucleotide == 'T':
		nucleotide = 'U'
		rna_seq = rna_seq + nucleotide
	else:
		rna_seq = rna_seq + nucleotide
print rna_seq


#task3 complementing a strand of DNA

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


#task4 Translating RNA into protein

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

rna_seq = raw_input()

#count the number of codons
codon_total_num = len(rna_seq)/3

#loop throuth the codons
#creat a list of codons
codon_list = []
for codon_num in range(0, codon_total_num):
	codon_start = codon_num * 3
	codon_end = codon_start + 3
	codon = rna_seq[codon_start:codon_end]
	codon_list.append(codon)
# print codon_list

#translate the codon into protein
protein = ''
stop_codon = ['UAA', 'UAG', 'UGA']
for codons in codon_list:
	if codons not in stop_codon:
		protein = protein + codon_table.get(codons)
	else:
		break
print protein



#task5 open reading frames(optional)

dna_file = ('rosalind_orf.txt', 'r')
dna_seq = ''
for line in dna_file:
    if line.startswith('>'):
	print 'header'
    else:
        line = line.rstrip
        dna_seq = dna_seq + str(line)

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
#look for start codon
if rna_seq.find('AUG') == -1:
	print 'there is no start codon'
else:
    import re
    start_points = [m.start() for m in re.finditer('AUG',rna_seq)]
    for start_m in start_points:
	cds = rna_seq[start_m:]
        
        #count the number of codons
        codon_total_num = len(cds)/3
        #creat a list of codons
        codon_list = []
        for codon_num in range(0, codon_total_num):
	    codon_start = codon_num * 3
	    codon_end = codon_start + 3
	    codon = cds[codon_start:codon_end]
	    codon_list.append(codon)
        #translate the codon into protein
        protein = ''
        stop_codon = ['UAA', 'UAG', 'UGA']
        for codons in codon_list:
	    if codons not in stop_codon:
                protein = protein + codon_table.get(codons)
	    else:
		break
        print protein


#loop throuth the codons in rev-DNA
#look for start codon
if rna_seq.find('AUG') == -1:
	print 'there is no start codon'
else:
    import re
    start_points = [m.start() for m in re.finditer('AUG',rna_rev)]
    for start_m in start_points:
	cds = rna_rev[start_m:]
        
        #count the number of codons
        codon_total_num = len(cds)/3
        #creat a list of codons
        codon_list = []
        for codon_num in range(0, codon_total_num):
	    codon_start = codon_num * 3
	    codon_end = codon_start + 3
	    codon = cds[codon_start:codon_end]
	    codon_list.append(codon)
        #translate the codon into protein
        protein = ''
        stop_codon = ['UAA', 'UAG', 'UGA']
        for codons in codon_list:
	    if codons not in stop_codon:
                protein = protein + codon_table.get(codons)
	    else:
		break
        print protein