#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Huizhi Lin (881125518130)
For Project of BIF50806 (2017)
"""

"""
Impoort the Modules that are needed in this project
"""
# for reading more than one files
import os
# for image manipulation functions
from scipy import misc 
# for edit arrays
import numpy as np
# for making plots
import matplotlib.pyplot as plt
# for clustering
# clustering with kmeans
from sklearn.cluster import KMeans
# clustering with Hierarchical Clustering(agglomerative)
from sklearn.cluster import AgglomerativeClustering
# for making animation of plots, from animation.py
import animation


"""
Create a list of filenames of the images
"""
# Define input files path
# Small test folder with 40 images (10 for each flower)
#path = 'test_flo/'
# Target folder with 209 images
path = 'Flowers/'
file_list = os.listdir(path)

if path == 'test_flo/':
    print('This is a test\n')
else:
    print('This is not a test, this is a analysis for 209 photos\n')



'''
Create functions for creat matrix
'''
# Create function for cropping images
# Crop off 100 pix from each sides
def crop_sides(image,numpix=100):
    return image[numpix:-numpix,numpix:-numpix,:]

# Create function for extract rgb features
# Return to a list include the mean value of each colour
def rgb_profile(image):
    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:,:,2]
    red_mean = np.mean(red.flatten())
    green_mean = np.mean(green.flatten())
    blue_mean = np.mean(blue.flatten())
    rgb_vector = [red_mean,green_mean,blue_mean]
    return rgb_vector

# Create functions for extract a long vector of colour information
# Create histograms for all colours
def plot_RGB_histograms(image):
    blue = image[:,:,2]
    green = image[:,:,1]
    red = image[:,:,0]
    blue_hist = np.histogram(blue.flatten(),normed=True)
    green_hist = np.histogram(green.flatten(),normed=True)
    red_hist = np.histogram(red.flatten(),normed=True)
    plt.plot(blue_hist[1][1:],blue_hist[0],color='blue')
    plt.plot(green_hist[1][1:],green_hist[0],color='green')
    plt.plot(red_hist[1][1:],red_hist[0],color='red')
    plt.show()   
# Creat a single vector that contain all information of the colour of the image
def hist_all_colors(image):
# first makes histograms of each color separately
    blue_hist = np.histogram(image[:,:,2].flatten(),normed= True)
    green_hist = np.histogram(image[:,:,1].flatten(),normed = True)
    red_hist = np.histogram(image[:,:,0].flatten(),normed = True) 
    # stacks them (horizontally) to form a single vector. 
    all_hist = np.hstack((red_hist[0],green_hist[0],blue_hist[0]))
    return all_hist

# Creat a function to calculate the Euclidean distance between two images
def euclid_dist_between_images(image1,image2):
    hist1 = hist_all_colors(image1)
    hist2 = hist_all_colors(image2)
    euclid_dist = np.sqrt(np.sum(np.square(hist1-hist2)))
    return euclid_dist

'''
# creat similarity matrix
# This process last two long!!!
# A seperate script called 'similarity_matrix.py' has been created for this task!
dis_list = []
sim_list = []
for n in range(len(file_list)):
    sub_list_dis = []
    sub_list_sim = []
    for m in range(len(file_list)):
        file_n = path + file_list[n]
        file_m = path + file_list[m]
        image_n = misc.imread(file_n,mode='RGB')
        image_m = misc.imread(file_m,mode='RGB')
        croped_image_n = crop_sides(image_n)
        croped_image_m = crop_sides(image_m)
        distance = euclid_dist_between_images(image_n,image_m)
        sub_list_dis.append(distance)
        sub_list_sim.append(1-distance)
    dis_list.append(sub_list_dis)
    sim_list.append(sub_list_sim)   
dis_matrix = np.array(dis_list)
sim_matrix = np.array(sim_list)
print(sim_matrix)
'''


'''
Clusting
Step 1 - Creat feature matrix
'''
# creat a feature matrix for clustering
# 30 float numbers for each image
matrix_plot = []
for file in file_list:
    file_name = path + file
    image = misc.imread(file_name,mode='RGB')
    croped_image = crop_sides(image)
    feature_vector = hist_all_colors(croped_image)
    matrix_plot.append(feature_vector)
feature_matrix = np.array(matrix_plot)
print('This is the feature matrix\n')
print(feature_matrix)

# creat a colour profile matix
# means of RGB for each image
matrix_rgb = []
for file in file_list:
    file_name = path + file
    image = misc.imread(file_name,mode='RGB')
    croped_image = crop_sides(image)
    vector_rgb = rgb_profile(croped_image)
    matrix_rgb.append(vector_rgb)
rgb_matrix = np.array(matrix_rgb)
print('\nThis is the rgb matrix with means for RGB\n')
print(rgb_matrix)


'''
Clusting
Step 2 - clusting
'''
# Creat a function for making a list of the clustering result
def clusting_list(clusting_result_array):
    c_list = ''
    for group_num in range(1,5):
        group = np.array(file_list)[clusting_result_array==group_num-1]
        group = np.sort(group)
        cluster = 'cluster' + str(group_num) + ' include: ' + ' '.join(group) + '\n'
        c_list += cluster
    return c_list


# clustering with kmeans on simple rgb profile
print('KMeans Clustering for rgb matrix\n')
x = rgb_matrix
kmeans = KMeans(n_clusters = 4, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)
#Creat a table with grouped images
result_list = clusting_list(y_kmeans)
print(result_list)      
#visualising the clusters
fig = plt.figure(figsize = (16,16))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[y_kmeans==0,0], x[y_kmeans==0,1], x[y_kmeans==0,2], c='grey', s = 70, label = 'cluster1')
ax.scatter(x[y_kmeans==1,0], x[y_kmeans==1,1], x[y_kmeans==1,2], c='red', s = 70, label = 'cluster2')
ax.scatter(x[y_kmeans==2,0], x[y_kmeans==2,1], x[y_kmeans==2,2], c='purple', s = 70, label = 'cluster3')
ax.scatter(x[y_kmeans==3,0], x[y_kmeans==3,1], x[y_kmeans==3,2], c='gold', s = 70, label = 'cluster4')
ax.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], kmeans.cluster_centers_[:,2], c='k', s = 70, label='centroids')
ax.set_title('Clusters of Flowers by K-Means Clustering', fontsize = 30)
ax.set_xlabel('red', fontsize = 30)
ax.set_ylabel('green', fontsize = 30)
ax.set_zlabel('blue', fontsize = 30)
fig.show()
# Create animation of the plots
angles = np.linspace(0,360,21)[:-1] # A list of 20 angles between 0 and 360
# create an animated gif (20ms between frames)
animation.rotanimate(ax,angles,'kmeans.gif',delay=20) 
# create a movie with 10 frames per seconds and 'quality' 2000
animation.rotanimate(ax,angles,'kmeans.mp4',fps=10,bitrate=2000)
# create an ogv movie
animation.rotanimate(ax,angles,'kmeans.ogv',fps=10) 


# clustering with Hierarchical Clustering(agglomerative) on simple rgb profile
print('Hierarchical Clustering for rgb matrix\n')
x = rgb_matrix
hc = AgglomerativeClustering(n_clusters = 4, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(x)
#Creat a table with grouped images
result_list = clusting_list(y_hc)
print(result_list)         
#visualising the clusters
fig = plt.figure(figsize = (16,16))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[y_hc==0,0], x[y_hc==0,1], x[y_hc==0,2], c='grey', s = 70, label = 'cluster1')
ax.scatter(x[y_hc==1,0], x[y_hc==1,1], x[y_hc==1,2], c='red', s = 70, label = 'cluster2')
ax.scatter(x[y_hc==2,0], x[y_hc==2,1], x[y_hc==2,2], c='purple', s = 70, label = 'cluster3')
ax.scatter(x[y_hc==3,0], x[y_hc==3,1], x[y_hc==3,2], c='gold', s = 70, label = 'cluster4')
ax.set_title('Clusters of Flowers by Hierarchical Clustering', fontsize = 30)
ax.set_xlabel('red', fontsize = 30)
ax.set_ylabel('green', fontsize = 30)
ax.set_zlabel('blue', fontsize = 30)
fig.show()
# Create animation of the plots
angles = np.linspace(0,360,21)[:-1] # A list of 20 angles between 0 and 360
# create an animated gif (20ms between frames)
animation.rotanimate(ax,angles,'hc.gif',delay=20) 
# create a movie with 10 frames per seconds and 'quality' 2000
animation.rotanimate(ax,angles,'hc.mp4',fps=10,bitrate=2000)
# create an ogv movie
animation.rotanimate(ax,angles,'hc.ogv',fps=10) 


# clustering with kmeans on colour profile matix
print('KMeans Clustering for feature matrix\n')
x = feature_matrix
kmeans = KMeans(n_clusters = 4, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans_feature = kmeans.fit_predict(x)
#Creat a table with grouped images
result_list = clusting_list(y_kmeans_feature)
print(result_list)       

# clustering with Hierarchical Clustering(agglomerative) on colour profile matix
print('Hierarchical Clustering for feature matrix\n')
x = feature_matrix
hc = AgglomerativeClustering(n_clusters = 4, affinity = 'euclidean', linkage = 'ward')
y_hc_feature = hc.fit_predict(x)
#Creat a table with grouped images
result_list = clusting_list(y_hc_feature)
print(result_list)

# END
print('The END')