# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:35:00 2017

@author: biegbart
"""

import random

random.seed()

lista = []
for i in range(0,100):
    lista.append(random.randrange(100))

#==============================================
bub = True
lbub = list(lista)
while(bub):
    bub = False
    for i in range (1,100):
        if (lbub[i-1]<lbub[i]):
            lbub[i-1],lbub[i]=lbub[i],lbub[i-1]
            bub = True

print(lista)
print(lbub)

#================================================


lwst1 = [lista[0]]
lwst2 = list(lista)
del lwst2[0]
while (len(lwst2)>0):
    i=0
    while((i<len(lwst1) and (lwst2[0]>lwst1[i]))):
        i+=1
    lwst1.insert(i,lwst2[0])
    del lwst2[0]
        
print(lwst1)        


        