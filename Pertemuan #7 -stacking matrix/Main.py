#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:14:14 2019

@author: rafliano
"""

import numpy as np


a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,2))
bMat = np.ones((2,2))

# stacking matrix, menumpuk matrix

c = np.hstack((a,b))
d = np.vstack((a,b))

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))

print(dMat)