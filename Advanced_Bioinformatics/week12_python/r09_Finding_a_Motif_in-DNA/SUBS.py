#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:34:11 2017
Rosalind exercise "Finding a Motif in DNA"
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
line_num = 0
for line in infile:
    line = line.strip('\n')
    if line_num == 0:
        seq = line
    if line_num > 0:
        sub_seq = line
    line_num += 1
infile.close()

# fnd the motif in sequences
pos_list = []
length = len(seq)
length_sub = len(sub_seq)
for start_point in range(length - length_sub):
    end_point = start_point + length_sub
    small_seq = seq[start_point:end_point]
    if small_seq == sub_seq:
        pos = start_point + 1
        pos_str = str(pos)
        pos_list.append(pos_str)
positions = ' '.join(pos_list)
print(positions)