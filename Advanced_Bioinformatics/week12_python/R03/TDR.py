#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:18:12 2017
Rosalind exercise "Transcribing DNA into RNA"
@author: evelina
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
        
#translate the dna into rna
rna_seq = dna_seq.replace('T','U')
print(rna_seq)