#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:38:49 2019

@author: rafliano
"""

import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array([23,14])

print(A)
print(Y)

A_inv = np.linalg.inv(A)

# menyelesaikan persamaan linear
X1 = np.dot(A_inv,Y)
print(X1)

# cara lain
X2 = np.linalg.solve(A,Y)
print(X2)