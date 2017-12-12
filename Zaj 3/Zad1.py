# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:52:59 2017

@author: biegbart
"""
import time
def silniaR(liczba):
    if (liczba>1):
        return (liczba*silniaR(liczba-1))
    else:
        return (1)

def silniaI(liczba):
    i = 1
    while (liczba>1):
        i = i*liczba
        liczba =liczba - 1
    return(i)

l = 900
temp = time.time()
silniaR(l)
print(time.time()-temp)
temp = time.time()
silniaI(l)
print(time.time()-temp)
