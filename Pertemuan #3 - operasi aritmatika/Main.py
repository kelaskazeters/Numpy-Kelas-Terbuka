#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:01:54 2019

@author: rafliano
"""

import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMTWISE operasion
# penjumlahan
hasil = anp + bnp

# pengurangan
hasil = anp - bnp

# perkalian
hasil = anp * bnp

# pembagian
hasil = anp / bnp

# kuadrat
hasil = anp**2

# multidimensi array numpy

c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil = c + d
hasil = c * d
print(hasil)