#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:49:24 2017
Rosalind exercise "Complementing a Strand of DNA"
@author: evelina
"""
import sys
test = False

# Define the input
if test == True:
    # Ask user input for a DNA sequence
    seq = input('Please enter a DNA sequence')
else:
    # Read the download file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')
    seq = ''
    for line in infile:
        line = line.strip('\n')
        seq += line

# Calculate the reverse complement DAN string
# exchange A-T and C-G
com_seq = seq.replace('A','t').replace('T','A').replace('t','T')
com_seq = com_seq.replace('C','g').replace('G','C').replace('g','G')
# reverse the sequence
rev_com_seq = com_seq[::-1]
print(rev_com_seq)