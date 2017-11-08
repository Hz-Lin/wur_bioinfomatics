#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:04:07 2017
Rosalind exercise "Translating RNA into Protein"
@author: evelina
"""

import sys
test = False

#define the input
if test == True:
    #ask user input for a sequence
    rna_seq = input('Please enter rna sequence')
else:
    #read the download file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')
    for line in infile:
        rna_seq = line.strip('\n')


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
      
#count the number of codons
codon_total_num = len(rna_seq)/3

#loop throuth the sequence and creat a list of codons
codon_list = []
for codon_num in range(0, int(codon_total_num)):
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
print(protein)
