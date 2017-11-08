#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:55:16 2017
For the exercise P2: Parsing
@author: Huizhi Lin (881125-518-130)
"""

# test setting
test = True

# Parse the file
# Read the  GenBank file
infile_name = 'argonaut.gb'
infile = open(infile_name,'r')
# Creat a list of asccession numbers and another list of organism names
list_accession = []
list_organism = []
for line in infile:
    line = line.strip()
    if line.startswith('ACCESSION'):
        accession = line.split()[1]
        list_accession.append(accession)
    elif line.startswith('ORGANISM'):
        organism = line.split('  ')[1]
        list_organism.append(organism)
if test==True:
    print(list_accession)
    print(len(list_accession))
    print(list_organism)
    print(len(list_organism))

# Read the  GenBank file
infile_name = 'argonaut.gb'
infile = open(infile_name,'r')
# Creat a list of sequences
list_sequence = []
begin = False
for line in infile:
    line = line.strip()
    if line.startswith('ORIGIN'):
        seq = ''
        begin = True
    elif line.startswith('//'):
        list_sequence.append(seq)
        begin == False
    else: 
        if begin == True:
            line = line.split()
            seq += ''.join(line[1:])
if test==True:
    print(list_sequence)
    print(len(list_sequence))
        
# Close the file
infile.close()



# Creat a function to calculate the GC content
def cal_gc(seq):
    gc_num = seq.count('g') + seq.count('c')
    gc_percentage = gc_num/len(seq)
    return(gc_percentage)

# Calculate lists of GC cotent and sequence length
list_gc = []
list_seqlen = []
for seq in list_sequence:
    gc = cal_gc(seq)
    seqlen = len(seq)
    list_gc.append(gc)
    list_seqlen.append(seqlen)
if test==True:
    print(list_gc)
    print(len(list_gc))
    print(list_seqlen)
    print(len(list_seqlen))

# Creat a dictionary with GC content as keys and other elements as values (in a list)
dic = {}
for n in range(len(list_gc)):
    gc = list_gc[n]
    gc_format = '%1.2f' % (gc*100) + '%'
    l = [list_accession[n],list_organism[n],gc_format,str(list_seqlen[n]),list_sequence[n]]
    dic[gc] = l
if test==True:
    print(dic)

# Create FASTA file
out_file_A = open('result_p2.fasta','w')
for key in sorted(dic.keys(),reverse=True):
    l = dic[key]
    header = '>' + l[0] + ' ' + l[1] + '\n'
    sequence = l[-1] + '\n'
    out_file_A.write(header)
    out_file_A.write(sequence)
    if test==True:
        print(header)
        print(sequence)
    
# Create text file
out_file_B = open('result_p2.txt','w')
for key in sorted(dic.keys(),reverse=True):
    l = dic[key]
    tab_line = '\t'.join(l[:4]) + '\n'
    out_file_B.write(tab_line)
    if test==True:
        print(tab_line)

# Close files
out_file_A.close()
out_file_B.close()