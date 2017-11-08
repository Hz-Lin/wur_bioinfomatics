#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:25:08 2017
Rosalind exercise "Computing GC Content"
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

# Creat a function to calculate the CG content
def cal_gc(seq):
    seq.upper
    gc_num = seq.count('G') + seq.count('C')
    gc_percentage = gc_num/len(seq)*100
    return(gc_percentage)

# Creat a function return to the corresponding key with a value
def get_key(dic,value):
    for key in dic.keys():
        if dic[key] == value:
            cos_key = key
    return(cos_key)
        

# parsing the file extact the ID and their CG content
# put them into two corressponding 
cd_dic = {}
seq = ''
rid = None
for line in infile:
    line = line.strip('\n')
    if line.startswith('>'):
        if rid != None:
            cd_dic[rid] = cal_gc(seq)
            seq = ''
        rid = line.strip('>')
    else:
        seq += line
# Add in the last pair of ID and CG content
cd_dic[rid] = cal_gc(seq)

# find the largest CG content, and print out the corresponding kay
# find the lagest value
value_list = list(cd_dic.values())
largest_val = max(value_list)
# get the corresponding id
rosalind_id = get_key(cd_dic,largest_val)

# print out result in format
print(rosalind_id)
print('%1.6f' % largest_val)