#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:46:55 2017
Rosalind exercise "Counting Point Mutations"
@author: evelina
"""

import sys
test = False

# Define the input
if test == True:
    # Use the sample FASTA file
    infile = open('sample.txt','r')
else:
    # Read the download FASTA file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')
# extract two sequenc strings
line_count = 0
for line in infile:
    line = line.strip('\n')
    if line_count == 0:
        seq_a = line
    else:
        seq_b = line
    line_count += 1

# Create a function to calculate the differnce count in two sequences
def cal_dif(seq1,seq2):
    dif_counts = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dif_counts += 1
    return(dif_counts)

# Calculate the difference from file
dif_num = cal_dif(seq_a,seq_b)
print(dif_num)
        