#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:26:40 2017

@author: Huizhi Lin (88112518130)
"""

# import modules
import sys
from Bio import Entrez
import parsing

# Function to parsing the file, and create a list of the ids
def parsing_input(infile_name):
    '''return a list of GeneBank ids
    
        infile_name: string, the name of a text file
    '''
    infile = open(infile_name,'r')
    # extact a list of ids
    id_list = []
    for line in infile:
        line = line.strip('\n')
        ids = line.split()
        for i in ids:
            id_list.append(i)
    return id_list


if __name__ == '__main__':
    infile_name = sys.argv[1]
    # extact a list of ids
    id_list = parsing_input(infile_name)
    
    # Retrieve the sequences from GenBank in GenBank format
    # using the BioPython Entrez module
    Entrez.email = "lin029@altschul.bioinformatics.nl"
    handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="gb")
    records = handle.read()
    print(records)

    # parsing the records and create output file
    list_accession = parsing.asc_num_list(records)
    list_organism = parsing.organ_name_list(records)
    list_sequence = parsing.seq_list(records)
    list_gc = parsing.cal_gc(list_sequence)
    list_seqlen = parsing.cal_len(list_sequence)
    dic = parsing.create_dic(list_accession,list_organism,list_gc,list_seqlen,list_sequence)
    parsing.write_output(dic)
    

