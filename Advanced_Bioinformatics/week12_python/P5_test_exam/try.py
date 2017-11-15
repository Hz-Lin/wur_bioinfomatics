#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 08:44:15 2017

@author: evelina
"""
import subprocess
import os.path

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

if __name__ == "__main__":
    run_needle('ref.fasta','related.fasta','out.needle')
    
'''
needle -asequence ref.fasta -bsequence related.fasta -gapopen 8 -gapextend 0.5 -outfile out.needle
'''