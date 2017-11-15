#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:51:13 2017
This is a script for the test Python exam for course BIF30806
@author: Huizhi Lin (881125518130)
"""

# import modules
import sys
import subprocess
import os.path

'''
Task 2: parse FASTA files with multiple protein sequences
and determinge the lengths of the sequences
'''
# function to parse the FASTA files
def parse_fasta(infile):
    '''return a dictionary with sequence labels as key and length as value
    
        infie: input fasta file
    '''
    len_dic = {}
    seq = ''
    label = None
    for line in infile:
        line = line.strip('\n')
        if line.startswith('>'):
            if label != None:
                len_dic[label] = len(seq)
                seq = ''
            label = line.split()[0]
            label = label[-10:].strip('>')
        else:
            seq += line
    # add the last key and value
    len_dic[label] = len(seq)
# need to solve the label problem of the last
    return len_dic

'''
Task 3: run the prgram needle to align the protein sequences
'''
def run_needle(infile_a,infile_b,outfile,gap_open=8,gap_extend=0.5):
    '''Create a needle output file
    
        infile_a: string the name of the FASTA file of reference protein sequences
        infile_b: string the name of the FASTA file of related protein sequences
        outfile: string, the name of output file
        gap_open: interger, default=8, gap open penalty (between 3 and 10) 
        gap_extend: float, default=0.5, gap extension penalty
    '''
    if gap_open<3 or gap_open>8:
        print('gap open penalty should between 3 and 10')
    if not os.path.exists(infile_a):
        raise ValueError('input file {0} does not exist'.format(infile_a))
    if not os.path.exists(infile_b):
        raise ValueError('input file {0} does not exist'.format(infile_b))

    cmd = 'needle -asequence %s -bsequence %s -gapopen %d -gapextend %1.1f -outfile %s'\
    % (infile_a,infile_b,gap_open,gap_extend,outfile)
    e = subprocess.check_call(cmd,shell=True)
    print('EXIT STATUS AND TYPE', e, type(e))
    return outfile

'''
Task 4: write a function to calculate the hamming distance of
two sequences of equal length
'''
def cal_distance(seq_a,seq_b):
    '''return to the hamming distance(interger) of seq_a and seq_b
    
        seq_a: string, a protein sequences
        seq_b: string, another protein sequences, same length as seq_a
    '''
    hamming_distance = 0
    if len(seq_a) != len(seq_b):
        print('The length of the two sequence are different!')
    else:
        for i in range(len(seq_a)):
            if seq_a[i] != seq_b[i]:
                hamming_distance += 1
    return hamming_distance


'''
Task 5: write a function to calculate the percent of identity
'''
def cal_identity(seq_a,seq_b):
    '''return to the percent of identity(float) of seq_a and seq_b
    
        seq_a: string, a protein sequences
        seq_b: string, another protein sequences, same length as seq_a
    '''
    indentity = 0    
    if len(seq_a) != len(seq_b):
        print('The length of the two sequence are different!')
    else:
        for i in range(len(seq_a)):
            if seq_a[i] == seq_b[i]:
                indentity += 1
        percent_identity = indentity/len(seq_a)*100
    return percent_identity


'''
Task 6: parse the needle output to estract all pairwise alignments
'''
# function to parse the neddle output file
def parse_needle(inflie):
    '''return a dictionary
        key: tuple, the labels of two aligned sequences
        values: tuple, the two aligned sequences
        
        infile: the output file from the needle program
    '''
    needle_dic = {}
    label1 = ''
    label2 = ''
    seq1 = ''
    seq2 = ''
    line_count = 0
    for line in inflie:
        line = line.strip('\n')
        if line:
            if not line.startswith('#'):
                if line_count%3 == 0:
                    label1 = line.split()[0]
                    sub_seq1 = line.split()[2]
                    seq1 += sub_seq1
                elif line_count%3 == 2:
                    label2 = line.split()[0]
                    sub_seq2 = line.split()[2]
                    seq2 += sub_seq2
                line_count += 1            
            elif line.startswith('#=='):
                if seq1 != '':
                    labels = (label1,label2)
                    seqs = (seq1,seq2)
                    needle_dic[labels] = seqs
                    seq1 = ''
                    seq2 = ''
                line_count = 0
            elif line.startswith('#--'):
                labels = (label1,label2)
                seqs = (seq1,seq2)
                needle_dic[labels] = seqs
    return needle_dic


'''
Task 7: report a tab-delimited tabel
'''
if __name__ == "__main__":
    
    # read the input files (Task 1)
    # fasta file with multiple protein sequences
    infile_name_related = sys.argv[1]
    # fasta file of the reference protein
    infile_name_ref = sys.argv[2]
    infile_related = open(infile_name_related,'r')
    infile_ref = open(infile_name_ref,'r')
    
    # parse the input files and calculate the sequence length
    len_dic_related = parse_fasta(infile_related)
    len_dic_ref = parse_fasta(infile_ref)
    
    # call the command line and create the needle output file
    run_needle('ref.fasta','related.fasta','out.needle')
    # parse the needle output file
    needle_file = open('out.needle','r')
    needle_dic = parse_needle(needle_file)
        
    
    # create the output file: tab-delimited table
    outfile = open('seq_ali_result.txt','w')
    # write the header
    header = 'Sequence1\tLength\tSequence2\tLength\tHamm\tIdent\n'
    outfile.write(header)
    # write the content lines
    for ref_label in len_dic_ref.keys():
        ref_seq_label = ref_label
        len_ref = len_dic_ref[ref_label]
    line_start = ref_seq_label + '\t' + str(len_ref) +'\t'
    for labels in needle_dic.keys():
        related_seq_label = labels[1]
        seq_a = needle_dic[labels][0]
        seq_b = needle_dic[labels][1]
        # calculate the hamm distance
        hamm = cal_distance(seq_a,seq_b)
        # calculate the identity
        ident = cal_identity(seq_a,seq_b)
        seq2_len = len_dic_related[related_seq_label]
        seq2_line = related_seq_label + '\t' + str(seq2_len) + '\t' + str(hamm) + '\t' + '%1.1f' % (ident) + '\n'
        out_line = line_start + seq2_line
        outfile.write(out_line)

    # close the files
    infile_related.close()
    infile_ref.close()
    outfile.close()