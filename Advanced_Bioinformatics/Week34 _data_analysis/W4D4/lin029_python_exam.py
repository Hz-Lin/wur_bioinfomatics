#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 09:01:30 2017
This is a script for the Python exam for course BIF30806
@author: Huizhi Lin (881125518130)
"""

# import modules
import sys
import subprocess
import os.path


# function: parsing GFF file
def parse_gff(infile):
    '''Return a dictionary with sequence labels as key and sequence as value
    
    Keyword arguments:
        infile -- gff file
    Returns:
        predict_protein -- dictionary, {label:sequence}
    '''
    predict_protein = {}
    seq = ''
    for line in infile:
        line = line.strip('\n')
        if not line:
            continue
        if line.startswith('# start gene'):
            seq_label = line.split()[3]
        elif line.startswith('# protein sequence'):
            seq = line.split()[4].strip('[')
        elif line.startswith('# end gene'):
            predict_protein[seq_label] = seq
        else:
            seq += line.strip('# ').strip(']')
    return predict_protein

# function: transfer a dictionary to FASTA file
def write_fasta(dic,outfile_name):
    '''Create a fasta file with key from the dictionary as header and
        values from the dictionary as sequence
    
    Keyword arguments:
        dic -- dictionary, {label:sequence}
        outfile_name -- string, the name of output fasta file
    Returns:
        ourfile_name.fasta -- fasta file
    '''
    outfile = open(outfile_name+'.fasta','w')
    for label,seq in dic.items():
        header = '>' + label + '\n'
        outfile.write(header)
        outfile.write(seq+'\n')
    outfile.close()
    return outfile
    
# function: run the programs makeblastdb and blastp in command line
def run_makedb(reference_file, db_name):
    '''Create a blast database, returen the database name
    
    Keyword arguments:
        reference_file -- reference file name to create the database
        db_name -- string,the name for the database
    Returns:
        db_name -- string, the database naem
    '''
    cmd_db = 'makeblastdb -dbtype prot -in %s -out yeast' % reference_file
    makeblastdb = subprocess.check_call(cmd_db,shell=True)
    print('EXIT STATUS AND TYPE', makeblastdb, type(makeblastdb))
    return db_name
        
def run_blast(query_file, db_name,outfile,output_format=7,num_ali=1):
    '''Create a blast output file
    
    Keyword arguments:
        query_file -- FASTA file contains the query protein sequences
        db_name -- string, the reference database name
        outfile, -- string, the name of output blast result file
        output_format -- integer, format of the output file, default = 7(tabular)
        num_ali -- integer, number of alignments, default = 1 
    Returns:
        ourfile -- the blast result file
    '''
    if os.path.exists(outfile):
        return outfile
    else:
        cmd_blast = 'blastp -query %s -db %s -out %s -outfmt %d -num_alignments %d'\
        % (query_file,db_name,outfile,output_format,num_ali)
        blastp = subprocess.check_call(cmd_blast,shell=True)
        print('EXIT STATUS AND TYPE', blastp, type(blastp))
    return outfile

# function: parse the resulting blast output
def parse_blast(blast_file):
    '''Return a dictionary with information from the blast result file
    
    Keyword arguments:
        blast_file -- inputfile, a blast result file
    Returns:
        dic_blast -- dictionary, format as below
        {query_id:[query_len,subject_id,percent_identity,align_len]}
    '''
    infile = open(blast_file,'r')
    dic_blast = {}
    for line in infile:
        line = line.strip('\n')
        if not line:
            continue
        if not line.startswith('#'):
            info = line.split('\t')
            query_id = info[0]
            query_len = int(info[3])
            subject_id = info[1]
            percent_identity = float(info[2])
            align_len = int(info[9]) - int(info[8]) + 1
            dic_blast[query_id] = [query_len,subject_id,percent_identity,align_len]
    infile.close()
    return dic_blast
    
# function: calculate the percent query coverage
def cal_pcov(aligned_length, total_length):
    '''Return the query coverage
    
    Keyword arguments:
        aligned_length -- integer, the length of the aligned part of the query
        total_length -- integer, the total query length
    Returns:
        pcov -- float, the percent query coverage
    '''
    pcov = (aligned_length/total_length)*100
    return pcov

# function: turn a dictionary into a tab-delimited file
def dic_to_tab(dic,out_file):
    '''Return a tab-delimited file
    
    Keyword arguments:
        dic -- dictionary, contains the information for the output
    Returns:
        out_file -- a tab-delimited file contains information from the dictionary
    '''   
    for key in sorted(dic.keys()):
        info = dic[key]
        out_line = key + '\t' + '\t'.join(info) + '\n'
        out_file.write(out_line)
    return out_file
    
    

if __name__ == "__main__":
    # read the filenames of the GFF file and the FASTA file
    if len(sys.argv) != 3:
        warning = 'Please use GFF and FASTA file names as arguments\n'
        sys.stdout.write(warning)
    else:
        infile_name_gff = sys.argv[1]
        infile_name_fasta = sys.argv[2]

    # extract the predicted protein sequences and store them in fasta
    infile_gff = open(infile_name_gff,'r')
    predict_protein = parse_gff(infile_gff)
    infile_gff.close()
    query_file = write_fasta(predict_protein,'predicted')
    
    # run the programs makeblastdb and blastp
    db_name = run_makedb(infile_name_fasta,'yeast')
    blast_file = run_blast(query_file,db_name,'yeast.blast')

    # parse the reslting blast output
    dic_blast = parse_blast(blast_file)
    
    # calculate the percent query coverage and add to the dictionary
    for qseqid,info_list in dic_blast.items():
        qcov = cal_pcov(info_list[-1], info_list[0])
        info_list[-1] = '%.2f' % qcov
        info_list[-2] = '%.2f' % info_list[-2]
        info_list[0] = str(info_list[0])
    
    # create a tabdelimited table
    result_file = open('result.txt','w')
    header = 'qseqid\tqlength\tsseqid\tpident\tqcov\n'
    result_file.write(header)
    dic_to_tab(dic_blast,result_file)
    result_file.close()
