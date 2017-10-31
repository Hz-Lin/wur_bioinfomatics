#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:08:08 2017

# @author: Huizhi Lin (881125518130)
# for Project BIF50806
# This script creat a similarity matrix and store it in a csv file
"""
# Impoort the Modules that are needed in this project
# for reading more than one files
import os
# for image manipulation functions
from scipy import misc 
# for edit arrays
import numpy as np

# Create a list of filenames of the images
# Define input files path
# Small test folder with 40 images (10 for each flower)
#path = 'test_flo/'
# Target folder with 209 images
path = 'Flowers/'
file_list = os.listdir(path)
file_list.sort()

if path == 'test_flo/':
    print('This is a test\n')
else:
    print('This is not a test, this is a analysis for 209 photos\n')
# Create output file
out_file = open('similarity_matrix.csv','w')

# Create function for croping images
def crop_sides(image,numpix=100):
    return image[numpix:-numpix,numpix:-numpix,:]

    
# Create a single vetor that contain all information of the colour of the image
def hist_all_colors(image):
# first makes histograms of each color separately
    blue_hist = np.histogram(image[:,:,2].flatten(),normed = True)
    green_hist = np.histogram(image[:,:,1].flatten(),normed = True)
    red_hist = np.histogram(image[:,:,0].flatten(),normed = True) 
    # stacks them (horizontally) to form a single vector. 
    all_hist = np.hstack((red_hist[0],green_hist[0],blue_hist[0]))
    return all_hist

# Create a function to  calculates the Euclidean distance between two images
def euclid_dist_between_images(image1,image2):
    hist1 = hist_all_colors(image1)
    hist2 = hist_all_colors(image2)
    euclid_dist = np.sqrt(np.sum(np.square(hist1-hist2)))
    return euclid_dist

# Create the csv file
out_file = open('similarity_matrix.csv', 'w')
header = ' \t' + '\t'.join(file_list) + '\n'
out_file.write(header)
# create similarity matrix
for n in range(len(file_list)):
    print(file_list[n]) #for tracking the process in concole
    sub_list_sim = [file_list[n]]
    for m in range(len(file_list)):
        file_n = path + file_list[n]
        file_m = path + file_list[m]
        image_n = misc.imread(file_n,mode='RGB')
        image_m = misc.imread(file_m,mode='RGB')
        croped_image_n = crop_sides(image_n)
        croped_image_m = crop_sides(image_m)
        distance = euclid_dist_between_images(image_n,image_m)
        similarity = '%2.2f' % (1-distance)
        sub_list_sim.append(similarity)
    line = '\t'.join(sub_list_sim) + '\n'
    out_file.write(line)

# Close the output file
out_file.close()