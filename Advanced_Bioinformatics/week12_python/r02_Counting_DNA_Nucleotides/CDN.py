#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:05:33 2017
Rosalind exercise "Counting DNA Nucleotides"
@author: Huizhi Lin
"""

import sys
test = False

#define the input
if test == True:
    #ask user input for a sequence
    dna_seq = input('Please enter dna sequence')
else:
    #read the download file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')
    for line in infile:
        dna_seq = line.strip('\n')

#count the numbers of bases
num_a = dna_seq.count('A')
num_c = dna_seq.count('C')
num_g = dna_seq.count('G')
num_t = dna_seq.count('T')
print(num_a,num_c,num_g,num_t)