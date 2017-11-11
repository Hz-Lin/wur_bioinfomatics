#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:55:16 2017
For the exercise P2: Parsing
@author: Huizhi Lin (881125-518-130)
"""

# Create a function to parsing the GenBank file and create a list of asccession numbers
def asc_num_list(infile_name):
    '''return list of asccession numbers
    
        infile_name: string, the name of a GeneBank format file
    '''
    infile = open(infile_name,'r')
    list_accession = []
    for line in infile:
        line = line.strip()
        if line.startswith('ACCESSION'):
            accession = line.split()[1]
            list_accession.append(accession)
    infile.close()
    return list_accession

# Create a function to parsing the GenBank file and create a list of organism names
def organ_name_list(infile_name):
    '''return list of organism names
    
        infile_name: string, the name of a GeneBank format file
    '''
    infile = open(infile_name,'r')
    list_organism = []
    for line in infile:
        line = line.strip()
        if line.startswith('ORGANISM'):
            organism = line.split('  ')[1]
            list_organism.append(organism)
    infile.close()
    return list_organism

# Create a function to parsing the GenBank file and create a list of sequence
def seq_list(infile_name):
    '''return list of DNA sequences
    
        infile_name: string, the name of a GeneBank format file
    '''
    infile = open(infile_name,'r')
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
    infile.close()
    return list_sequence

    
# Creat a function to calculate the GC content
def cal_gc(seq_list):
    '''return a list of the GC content percentage of DNA sequences
        
        seq_list: list, a list of DNA sequence
    '''
    list_gc = []
    for seq in seq_list:
        gc_num = seq.count('g') + seq.count('c')
        gc_percentage = gc_num/len(seq)
        list_gc.append(gc_percentage)        
    return list_gc

# Creat a function to calculate the sequence length
def cal_len(seq_list):
    '''return a list of the sequence length of the DNA seqences
        
        seq_list: list, a list of DNA sequence
    '''
    list_seqlen = []
    for seq in seq_list:
        seqlen = len(seq)
        list_seqlen.append(seqlen)        
    return list_seqlen

# Function to create a dictionary with GC content as keys and other elements as values (in a list)
def create_dic(list_accession,list_organism,list_gc,list_seqlen,list_sequence):
    '''retun a dictionary with GC content as keys and other elements as values
    
        list_accession:list, list of asccession numbers
        list_organism:list, list of organism names
        list_gc:list, list of the GC content percentage
        list_seqlen:list, list of the sequence length
        list_sequence:list, list of DNA sequences
        '''
    dic = {}
    for n in range(len(list_gc)):
        gc = list_gc[n]
        gc_format = '%1.2f' % (gc*100) + '%'
        l = [list_accession[n],list_organism[n],gc_format,str(list_seqlen[n]),list_sequence[n]]
        dic[gc] = l
    return dic

# Function to create output files
def write_output(dic):
    '''Produces a FASTA file with the sequences and a tab-delimited file
    
        dic: dictionary, a dictionary with GC content as keys and other elements as values
    '''
    # Create FASTA file
    out_file_A = open('result_p2.fasta','w')
    for key in sorted(dic.keys(),reverse=True):
        l = dic[key]
        header = '>' + l[0] + ' ' + l[1] + '\n'
        sequence = l[-1] + '\n'
        out_file_A.write(header)
        out_file_A.write(sequence)   
    # Create text file
    out_file_B = open('result_p2.txt','w')
    for key in sorted(dic.keys(),reverse=True):
        l = dic[key]
        tab_line = '\t'.join(l[:4]) + '\n'
        out_file_B.write(tab_line)
    # Close files
    out_file_A.close()
    out_file_B.close()