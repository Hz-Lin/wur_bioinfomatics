#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:20:24 2017
Rosalind exercise "Open Reading Frames"
@author: evelina
"""

import sys
test = False

# Define the input
if test == True:
    # Use the sample FASTA file
    infile = open('sample.fasta','r')
else:
    # Read the download FASTA file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')

# extact the sequences out of the file
dna_seq = ''
line_num = 0
for line in infile:
    if line_num > 0:
        line = line.strip('\n')
        dna_seq = dna_seq + str(line)
    line_num += 1
infile.close()

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

# Creat a function to transcribe DNA to RNA
def dna_to_rna(dna):
    rna = ""
    for nucleotide in dna:
        if nucleotide == 'T':
            nucleotide = 'U'
            rna = rna + nucleotide
        else:
            rna = rna + nucleotide
    return(rna)

#transcribe the dna strand
rna_seq = dna_to_rna(dna_seq)
rna_rev = dna_to_rna(dna_rev)
 
   
# Creat a function to translate RNA to protein

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

# orf can be 0 or 1 or 2
# 0:start with the first base; 1:start with the second base; 3:start with the third base
def rna_to_protein(rna,orf):
    #loop throuth the codons in a orf
    codon_list = []
    codon_total_num = int(len(rna) - orf/3)
    for codon_num in range(0, codon_total_num):
        codon_start = codon_num * 3 + orf
        codon_end = codon_start + 3
        codon = rna[codon_start:codon_end]
        codon_list.append(codon)
    #translate the codon into protein
    protein = ''
    pro_list = []
    for codons in codon_list:
        protein = protein + str(codon_table.get(codons))
    #looking for valid sequence
    for n in range(len(codon_list)):
        if protein[n] == 'M':
            m = protein.find('*',n)
            if m != -1:
                pro = protein[n:m]
                pro_list.append(pro)
    return(pro_list)

# Translate two rna strands into valid protein sequences
protein_list = []
for orf in range(3):
    pro_orf = rna_to_protein(rna_seq,orf) + rna_to_protein(rna_rev,orf)
    for pro in pro_orf:
        if pro not in protein_list:
            protein_list.append(pro)

# Print out the results
result = '\n'.join(protein_list)
print(result)