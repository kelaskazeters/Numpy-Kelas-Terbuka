#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:00:07 2019

@author: rafliano
"""

import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[3,4,5]), dtype = float)

# membuat matrix dengan menggunakan function

def kuadrat(baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return kolom + baris

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)

# membuat array atau matrix dengan menggunakan iterable

iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype = int)

# meltitype array

dtipe = [('nama','S255'), ('tinggi', int)]

data = [
        ('ucup', 150),
        ('ali', 160),
        ('maria', 180)
]

e = np.array(data, dtype = dtipe)

print(e[0])