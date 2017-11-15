#!/usr/bin/env python3

"""
Author: Yan Wang
Student number:951104927110
Align refrence sequence with multipul sequence, and output a file including
their length, hamming distance, and identity.
"""

from sys import argv
import subprocess
import os.path

def parse_fasta(fasta):
    '''parse a fasta file, return a dictionary: {identifier:seq}
    
    fasta: file
    '''
    seqs_dict = {}
    for line in fasta:
        if not line.strip():
            continue
        else:
            if line.startswith('>'):
                identifier = line[1:].split()[0]
                seqs_dict[identifier] = ''
            else:
                seqs_dict[identifier] += line.strip()
            
    return seqs_dict
    
def run_needle(ref_f, db_f, gapopen=8, gapextend=0.5, out_f='out.needle'):
    '''Using needle to align sequences
    Return the name of output file.
    
    ref_f, db_f: file, reference sequence file and database sequence file
    out_f: output file
    '''          
    cmd = r'needle %s %s -gapopen %f -gapextend %f %s' % (ref_f, db_f, gapopen, gapextend, out_f)
    if not os.path.exists(out_f):
        subprocess.check_call(cmd, shell=True)
    return out_f
    
def hamming(seq1, seq2):
    '''Return the hamming distance of two sequence
    
    seq1, seq2: string, dna sequences
    '''
    hamm = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]: hamm += 1
    return hamm
    
def perc_identity(seq_a, seq_b):
    '''Return the identity of two aligned sequence
    
    seq_a, seq_b: string, aligned sequence
    '''
    num_id_pos = len(seq_a) - hamming(seq_a, seq_b)
    percent = num_id_pos / len(seq_a) * 100
    return percent
    
def parse_needle(needle):
    '''parse needle file to extract pairwise alignment, 
    return a dict: {(seq1,seq2):(sequence1,sequence2)}
    
    needle: file, a .needle file
    '''
    aligned_pair = {}
    for line in needle:
        if not line.strip():
            i = 0
            continue
        else:
            if line.startswith('#==='):
                sequence1 = ''
                sequence2 = ''
            if not line.startswith('#'):
                if i == 0:
                    seq1 = line.split()[0]
                    sequence1 += line.split()[2]
                if i == 2:
                    seq2 = line.split()[0]
                    sequence2 += line.split()[2]
                    aligned_pair[(seq1,seq2)]= (sequence1,sequence2)
                i += 1
    return aligned_pair
    
#def ident_dict(aligned):
    '''Return a dictionary of identity of two sequence, {(seq1, seq2):identity}
    
    aligned: dict, dict obtained from function:parse_needle
    '''
    ident = {}
    for key in aligned:
        identity = perc_identity(aligned[key][0],aligned[key][1])
        ident[key] = identity
    return ident
        
def report(ref_seq, db_seqs, aligned, output):
    '''Return the report file, a tab-delimite file
    
    ref_seq, db_seqs: dict, dictionary of reference sequence and database sequences
    aligned: dict, dictionary of aligned seq pair, obtained from function parse_needle
    ident: dict, identity of paired sequence, obtained from function ident_dict
    output: file
    '''
    output.write('%10s\t%6d\t%10s\t%6d\t%4d\t%-5d\n'.format('Sequence1', 'Length', 'Sequence2', 'Length', 'Hamm', 'Ident'))
    for key1 in ref_seq:
        for key2 in db_seqs:
            seq1 = aligned[(key1,key2)][0]
            seq2 = aligned[(key1,key2)][1]
            hamm = hamming(seq1,seq2)
            identity = perc_identity(seq1,seq2)
            output.write('%-10s\t%-6d\t%-10s\t%-6d\t%-4d\t%-5.1f\n' % (key1,len(seq1),key2,len(seq2),hamm,identity))


if __name__ == '__main__':
    with open(argv[1]) as ref:
        ref_dict = parse_fasta(ref)
        print(ref_dict)
    
    with open(argv[2]) as related:
        related_dict = parse_fasta(related)
        gapopen,gapextend,out_f = 8, 0.5,'out.needle'
        needle_outp = run_needle(argv[1], argv[2], gapopen, gapextend, out_f)
        print(related_dict)
        
    with open(needle_outp) as needle:  
        aligned_pair = parse_needle(needle)
        print(aligned_pair)
    
    with open(argv[3],'w') as result:
        report(ref_dict, related_dict, aligned_pair, result)
