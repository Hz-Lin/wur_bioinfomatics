#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:51:13 2017
This is a script for the clustering exercise
@author: Huizhi Lin (881125518130)
"""

# import Python modules
import sys
import numpy
import scipy
import scipy.cluster.hierarchy as sch
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# TXT file parser
def txt_parse(file_path):
    '''returen to a Pandas DataFrame
    
        file_path:string, the path of the tab-detimited TXT file
    '''
    infile = open(file_path,'r')
    line_count = 0
    gene_names = []
    dic = {}
    for line in infile:
        line = line.strip('\n')
        if line_count == 0:
            header = line.split('\t')
        else:
            line = line.split('\t')
            gene_names.append(line[0])
            for i in range(1,len(header)):
                dic_key = header[i]
                expression = float(line[i])
                if dic_key not in dic.keys():
                    dic[dic_key] = [expression]
                else:
                    dic[dic_key].append(expression)
        line_count += 1
    df = pd.DataFrame(dic, index=gene_names)
    return df

# hierarchical clustering
def hc_clus(df,distance_metric,linkage='complete'):
    '''return the clustering result
        
        df: dataframe, a Pandas dataframe
        distance_metric: string, 'euclidean', 'correlation', etc
        linkage: string, linkage methods
    '''
    distances = sch.distance.pdist(df, metric=distance_metric)
    print(distances.shape)
    clustering = sch.linkage(distances, method=linkage)
    return clustering



if __name__ == "__main__":
    
    # read input txtfile and create the Pandas DataFrame
    infile = sys.argv[1]
    df = txt_parse(infile)
    # clustering the data by sample
    df_trans = df.transpose()
    sample_clustering = hc_clus(df_trans,'euclidean')
    sample_names = list(df_trans.index)
    sample_tree = sch.dendrogram(sample_clustering,labels=sample_names)
#    plt.savefig('sample_dendrogram.pdf', format="PDF")
    # clustering the data by genes
    gene_clustering = hc_clus(df, 'correlation')
    gene_names = list(df.index)
    gene_tree = sch.dendrogram(gene_clustering, leaf_font_size=2, color_threshold=4,labels=gene_names)
#    plt.savefig('gene_dendrogram.pdf', format="PDF")
    # clustered heatmap
    sns.set(color_codes=True)
    heatmap = sns.clustermap(df,method='complete',figsize=(18,20),col_cluster=False)
    plt.savefig('heatmap.pdf', format="PDF")
