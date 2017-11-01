#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:31:11 2017

@author: evelina
"""

import sys

numbers = sys.argv[1:]
sumary=0
out_line = ""
for num in numbers:
    num = int(num)
    sumary += num
out_line = '+'.join(numbers) + " = " + str(sumary)
print(out_line)