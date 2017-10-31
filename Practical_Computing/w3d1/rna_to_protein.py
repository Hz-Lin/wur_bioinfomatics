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
	

