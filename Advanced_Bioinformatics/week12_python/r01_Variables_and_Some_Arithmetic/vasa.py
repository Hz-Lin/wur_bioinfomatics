#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:33:32 2017
Rosalind exercise "Variables and Some Arithmetic"
@author: Huizhi Lin
"""
import sys
test = False

#define the values of a and b
if test == True:
    #ask user input for values
    a = int(input('Please enter a positive number a'))
    b = int(input('Please enter a positive number b'))
else:
    #read the download file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')
    for line in infile:
        line = line.strip('\n')
        num_list = line.split()
        a = int(num_list[0])
        b = int(num_list[1])

#create the function to calculate the square of the hypotenuse 
#of the right triangle whose legs have lengths aa and bb
def triangle_cal(n1,n2):
    square_n3 = n1**2 + n2**2
    return(square_n3)

if a<0 or b<0:
    print('numbers must be positive')
elif a>1000 or b>1000:
    print('numbers must be smaller than 1000')
else:
    c = triangle_cal(a,b)
    print(c)
