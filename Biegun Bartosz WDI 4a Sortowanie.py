# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:35:00 2017

@author: biegbart
"""

import random

random.seed()

#----------------------------------------------------------------------
#----------  n - liczba el. w tablicy do posortowania  ----------------
#----------------------------------------------------------------------

n = 50

#========================

def quicksort(tab,l,r):
    
    def podzieltab(tab,l,r):           
        indpodz = l + (r-l)//2 # wyb.punkt podziału
        wartpodz = tab[indpodz]
        tab[indpodz],tab[r] = tab[r],tab[indpodz]
        
        apoz = l #aktualna pozycja
        
        for i in range (l,r):
            if (tab[i]<wartpodz):
                tab[i],tab[apoz] = tab[apoz],tab[i]
                apoz+=1
        tab[apoz],tab[r] = tab[r],tab[apoz]
        return apoz
    
    
    if (l<r):
        i=podzieltab(tab,l,r)
        quicksort(tab,l,i-1)
        quicksort(tab,i+1,r)
    

#===================
#Mergesort

def mergesort(tabA,tabB,n):
    def zlacz(tabA,istart,ipodz,iend,tabB):
        i = istart
        j = ipodz
        
        for x in range(istart,iend):#!!!!!!!!!!!!!!!!!!!!!
            if ((i < ipodz) and ((j >= iend) or (tabA[i] <= tabA[j]))):
                tabB[x]=tabA[i]
                i+=1
            else:
                tabB[x]=tabA[j]
                j+=1
                
        
    def podziel(tabB,istart,iend,tabA):
        if (iend - istart > 1):
            ipodz = (istart + iend)//2 #punkt podziału listy
            podziel(tabA,istart,ipodz,tabB)
            podziel(tabA,ipodz,iend,tabB)
            zlacz(tabB,istart,ipodz,iend,tabA)
    
    
    tabB=list(tabA)
    podziel(tabB,0,n,tabA)

#==========================================================
#kopcowe
    
def heapsort(tab,n):
    
    def kopcujp(tab,n,i):
        mx = i #największy
        l = 2*i+1
        r = 2*i+2
        
        if ((l>n)and(tab[l]>tab[mx])):
            tab[i],tab[l] = tab[l],tab[i]
            kopcujp(tab,n,l)
        if ((r>n)and(tab[r]>tab[mx])):            
            tab[i],tab[r] = tab[r],tab[i]
            kopcujp(tab,n,r)
        
        if (mx != i):
            tab[i],tab[mx] = tab[mx],tab[i]            
    
    def kopcuj(tab,n,i):
        mx = i #największy
        l = 2*i+1
        r = 2*i+2
        
        if ((l<n)and(tab[l]>tab[mx])):
            mx = l
        if ((r<n)and(tab[r]>tab[mx])):
            mx = r
        
        if (mx != i):
            tab[i],tab[mx] = tab[mx],tab[i]
            kopcuj(tab,n,mx)
    
    for i in range((n//2)-1,-1,-1):
        kopcuj(tab,n,i)
    for i in range (n-1,-1,-1):
        tab[0],tab[i]=tab[i],tab[0]
        kopcuj(tab,i,0)               
        
#===============================================

def Selectionsort(tab,n):
    def zmax(tab,n): # znajdz max element
        mx=0
        for i in range (0,n):
            if (tab[i]>tab[mx]):
                mx=i
        return mx
    
    for i in range (n,1,-1):
        mx = zmax(tab,i)
        if (mx != i-1):
            tab[i-1] ,tab[mx]=tab[mx],tab[i-1]

#================================
            
def bubsort(lbub,n):
    
    bub = True
     
    while(bub):
        bub = False
        for i in range (1,n):
            if (lbub[i-1]>lbub[i]):
                lbub[i-1],lbub[i]=lbub[i],lbub[i-1]
                bub = True
#=======================================================
def wstawsort(lst):
    i = 0
    lwst2 = list(lst)        
    lst = [lst[0]]
    
    del lwst2[0]
    while (len(lwst2)>0):
        i=0
        while((i<len(lst) and (lwst2[0]>lst[i]))):
            i+=1
        lst.insert(i,lwst2[0])
        del lwst2[0]
    return lst    
    #print(lst)


#=====================================
            
lista = []
for i in range(0,n):
    lista.append(random.randrange(100))

#==============================================
"""
    
    #print(lbub)

#================================================


  
"""      
#=============================================
print("Oryginalna:",lista)
ls= list(lista)
lwst4 = list(lista)

ls= wstawsort(ls)
print("Wstawianie:",ls)

ls= list(lista)
heapsort(ls,n)
print("Kopcowanie:",ls)

ls= list(lista)
Selectionsort(ls,n)
print("Wybieranie:",ls)

ls= list(lista)
bubsort(ls,n)
print("Bublesort :",ls)  

ls= list(lista)
mergesort(ls,lwst4,n)
print("Mergesort :",ls)

ls= list(lista)
mergesort(ls,lwst4,n)
print("Quicksort :",ls)
      