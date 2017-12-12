# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:52:59 2017

@author: biegbart
"""
import time
def fibR(liczba):
    if (liczba>1):
        return (fibR(liczba-2)+fibR(liczba-1))
    else:
        return (1)

def fibI(liczba):
    i = 1
    j = 1
    temp = 0
    while (liczba>1):
        temp = i+j
        i = j
        j = temp
        liczba =liczba - 1
    return(temp)

l = 4
temp = time.time()
r=fibR(l)
print(time.time()-temp)
temp = time.time()
i=fibI(l)
print(time.time()-temp)
