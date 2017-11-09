#!/usr/bin/env python3

'''
This is a script for P3.
Created on 08-11-2017
Created by:
- Huizhi Lin (881125-518-130)
- MRN Akhand (860512-007-030)
'''


# set test status
test = False

# input file
if test == True:
    infile_name ='tiny.fq'
else:
    infile_name = 'tomatosample.fq'

infile_org = open(infile_name,'r')
infile_tri = open('trimmed.fq','r')
outfile = open('result_p3.txt','w')

# Parsing the input file
# exact the sequence and their quality line into a dictionary
# Creat a function to parsing the input file
def parsing(infile):
    '''return a dictionary with seq_number as key, seq and quality seq as values
        infile_name:object, the input file
    ''' 
    dic = {}
    line_count = 0
    seq_num = 1
    for line in infile:
        line = line.strip('\n')
        if line_count%4==1:
            seq = line
        elif line_count%4==3:
            quality_line = line
            dic[seq_num] = [seq,quality_line]
            seq_num += 1
        line_count += 1
    return dic

# Create a list contain all the sequence
def seq_list(dic):
    '''return a list of all the sequences
        dic: dictionary, dictionary created from the function parsing
    '''
    seq_list = []
    for key in list(dic.keys()):
        seq = dic[key][0]
        seq_list.append(seq)
    return seq_list

# Create a list contain all the quality lines
def quality_list(dic):
    '''return a list of all the quality lines
        dic: dictionary, dictionary created from the function parsing
    '''
    quality_list = []
    for key in list(dic.keys()):
        quality_line = dic[key][1]
        quality_list.append(quality_line)
    return quality_list    

# create a function to calulate the longest, shortest and averate seqence length
def cal_len (seq_list):
    '''return a string of longest, shortest and averate seqence length
        seq_list: a list or sequences
    '''
    len_total = 0
    len_list = []
    for seq in seq_list:
        seq_len = len(seq)
        len_total += seq_len
        len_list.append(seq_len)
    len_list.sort()
    max_len = len_list[0]
    min_len = len_list[-1]
    avg_len = len_total/len(len_list)
    out_string = 'min=%d, max=%d, avg=%1.2f' % (max_len,min_len,avg_len)
    return out_string 

# Create a function to create a nested list of all sequence's quality
def nest_quality(quality_list):
    '''return a list with quality_value_list nested in
        quality_list: list, created by quality_list() function
    '''
    list_quality = []
    for qua_seq in quality_list:
        quality_value_list = []
        for i in qua_seq:
            quality = ord(i) - 64
            quality_value_list.append(quality)
        list_quality.append(quality_value_list)
    return list_quality

# Create a function to calulate the average quality score at each position
def avg_quality(list_quality):
    '''return a list of qulaity values corresponding to the position
        list_quality: list, with quality_value_list nested in
    '''
    # calculate the longest seq
    longest_len = 0
    for quality_value_list in list_quality:
        if len(quality_value_list) > longest_len:
            longest_len = len(quality_value_list)
    # calculate the average quality score
    quality_avg_list=[]
    for i in range(longest_len):
        pos_total_quali = 0
        quali_count = 0
        for quality_value_list in list_quality:
            if i < len(quality_value_list):
                pos_total_quali += quality_value_list[i]
                quali_count += 1
        pos_quali_avg = pos_total_quali/quali_count
        quality_avg_list.append(pos_quali_avg)
    return quality_avg_list

if __name__ == "__main__":
    # caculation on the original file
    dic_org = parsing(infile_org)
    seq_list_org = seq_list(dic_org)
    quality_list_org = quality_list(dic_org)
    summary_org = cal_len(seq_list_org)
    list_quality_org = nest_quality(quality_list_org)
    quality_avg_list_org = avg_quality(list_quality_org)
    # caculation on the trimmed file
    dic_tri = parsing(infile_tri)
    seq_list_tri = seq_list(dic_tri)
    quality_list_tri = quality_list(dic_tri)
    summary_tri = cal_len(seq_list_tri)
    list_quality_tri = nest_quality(quality_list_tri)
    quality_avg_list_tri = avg_quality(list_quality_tri)
    # Close the inputfiles
    infile_org.close()
    infile_tri.close()
    
    # Create out put file
    # summaries
    outline_summary_org = 'ORIGINAL: ' + summary_org + '\n'
    outfile.write(outline_summary_org)
    outline_summary_tri = 'TRIMMED: ' + summary_tri + '\n'
    outfile.write(outline_summary_tri)
    # detail informations on different positions
    for pos in range(len(quality_avg_list_org)):
        order = str(pos + 1)
        if pos < len(quality_avg_list_tri):
            org = quality_avg_list_org[pos]
            tri = quality_avg_list_tri[pos]
            diff = tri - org
            outline = order + '\t%1.2f' % org + '\t%1.2f' % tri + '\t%1.2f' % diff + '\n'
            outfile.write(outline)
        else:
            org = quality_avg_list_org[pos]
            outline = order  + '\t%1.2f' % org + 'NA' + 'NA\n'
            outfile.write(outline)
    # Close output file
    outfile.close()