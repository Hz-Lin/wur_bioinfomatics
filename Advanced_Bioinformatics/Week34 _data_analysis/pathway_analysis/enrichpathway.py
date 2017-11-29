#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:01:30 2017

@author: Huizhi Lin (881125518130)
"""

# import Python modules
import sys
import scipy.stats

# get a dictionary with pathway description as key and pathway id as value
infile_pathway = open('Pathways.txt','r')
dic_pathway = {}
path_des = {}
for line in infile_pathway:
    line = line.strip('\n')
    if line.startswith('map'):
        line = line.split('\t')
        pathway_id = line[0]
        description = line[1]
        dic_pathway[description] = pathway_id
        path_des[pathway_id] = description
infile_pathway.close()

# get a dictionary with ec number as key and pathway description as value
infile_ec = open('EC2KEGG.txt','r')
dic_ec = {}
for line in infile_ec:
    line = line.strip('\n')
    line = line.split('\t')
    if line[0] != '':
        ec_number = line[0]
        kegg = line[1].split(';')
        desciption = kegg[0]
        dic_ec[ec_number] = desciption
infile_ec.close()

# parse the gene expression data
infile_gene = open('GeneExpressionData.txt','r')
over_total = 0
geno_total = 0
# ec number as key and count as values
dic_over = {}
dic_geno = {}
for line in infile_gene:
    line = line.strip('\n')
    if line.startswith('SCLAV'):
        geno_total += 1
        line = line.split('\t')
        if line[-1] == 'yes':
            over_total += 1
            if line[3] != '':
                ec_number = line[3]
                if ec_number in dic_over.keys():
                    dic_over[ec_number] += 1
                else:
                    dic_over[ec_number] = 1
                if ec_number in dic_geno.keys():
                    dic_geno[ec_number] += 1
                else:
                    dic_geno[ec_number] = 1
                
        else:
            if line[3] != '':
                ec_number = line[3]
                if ec_number in dic_geno.keys():
                    dic_geno[ec_number] += 1
                else:
                    dic_geno[ec_number] = 1
infile_gene.close()


# create dictionaries with pathway id as keys and counts [over,geno] as values
pathway_count = {}
for ec_number in dic_over.keys():
    if ec_number in dic_ec.keys():
        description = dic_ec[ec_number]
        description = description.strip('"')
        if description in dic_pathway.keys():
            pathway_id = dic_pathway[description]
            over_count = dic_over[ec_number]
            geno_count = dic_geno[ec_number]
            if pathway_id in pathway_count.keys():
                pathway_count[pathway_id][0] += over_count
                pathway_count[pathway_id][1] += geno_count
            else:
                pathway_count[pathway_id] = [over_count,geno_count]  

# perform fishers exact test for each pathways
path_list = list(pathway_count.keys())
path_list.sort()
out_file = open('result.txt','w')
# Bonfernoni significant level
bonfernoni = 0.05/len(path_list)
header = 'KEGG pathway\tDescription\tp-value\tsignificant base on p-value\tsignificant after FDR\n'
out_file.write(header)
for pa in path_list:
    test_table = [[pathway_count[pa][0],over_total],[pathway_count[pa][1],geno_total]]
    oodsration,p_value = scipy.stats.fisher_exact(test_table)
    if p_value <0.05:
        sig = 'yes'
        if p_value < bonfernoni:
            sig_bon = 'yes'
        else:
            sig_bon = 'no'
    else:
        sig = 'no'
    out_line = pa + '\t' + path_des[pathway_id] + '\t' + str(p_value) + '\t' + sig + '\t' + sig_bon + '\n'
    out_file.write(out_line)
out_file.close()
        


            
