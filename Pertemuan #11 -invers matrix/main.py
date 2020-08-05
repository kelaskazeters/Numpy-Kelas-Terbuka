#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:36:39 2019

@author: rafliano
"""

import numpy as np

a = np.array([(1,-1),(1,1)])

print(a)

# inverse matrix
a_inv = np.linalg.inv(a)

print(a_inv)

# determinan matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)
