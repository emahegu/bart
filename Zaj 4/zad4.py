# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:52:59 2017

@author: biegbart
"""

# MAX <=> liczba

import time
liczba = 25
for pot in range(1,10):
    liczba = liczba * 2
    temp = time.time()
    tab= []
    for i in range(1,liczba):
        tab.append(1)

    for i in range(1,liczba):
        l=2*i
        while (2*l < liczba+1):
            tab[l]=0
            l+=1

    print(liczba,'   ',time.time()-temp)

