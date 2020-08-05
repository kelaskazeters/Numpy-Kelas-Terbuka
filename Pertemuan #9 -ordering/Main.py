#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:37:57 2019

@author: rafliano
"""

import numpy as np

a = np.floor(np.random.randn(1,6)*10)

print(a)

print('nilai max dari a = ',a.max())
print('posisi max dari a = ',a.argmax())
print('nilai min dari a = ',a.min())
print('posisi min dari a = ',a.argmin())

print('mengurutkan nilai a:')
print(np.sort(a))
print(np.argsort(a))