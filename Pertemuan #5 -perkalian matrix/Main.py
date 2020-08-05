#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:41:01 2019

@author: rafliano
"""

import numpy as np

a = np.array(([1,2], 
              [3,4]))
b = np.ones([2,2])

print("matrix a:")
print(a)

print("matrix b:")
print(b)

# perkalian matrix
c1 = np.dot(a,b)
c2 = a.dot(b)

print("matrix c:")
print(c2)