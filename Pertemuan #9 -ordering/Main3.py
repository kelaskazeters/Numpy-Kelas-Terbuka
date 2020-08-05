#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:10:51 2019

@author: rafliano
"""

import numpy as np

dtipe = [('nama','S10'),('tinggi',int)]
data = [('Ucup',170),
        ('Ali',150),
        ('Mario',160)
]

a = np.array(data, dtype = dtipe)
print(a)

print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))