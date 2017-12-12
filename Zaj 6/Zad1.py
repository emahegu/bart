# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:44:55 2017

@author: biegbart
"""
#def przes(znak,przes):
    
def cezar(txt,przes):
    znak=''.join([(chr(((ord(i)-97+przes) % 26)+97)) for i in txt]) 
    return znak


def brutus(txt,przes):
    return cezar(txt.przes*(-1))

def podstawieniowy(txt,alfabet):
    result = ''.join([(chr((ord(i)-97+list(alfabet)[ord(i)-97] % 26)+97))  for i in txt]) 
    

def SKlucz(txt,klucz):
    lista = []
    for i in range (0,list(txt).length):
        lista.append((chr(((ord(i)-97+ord(list(klucz)[i % (list(klucz).length)])) % 26)+97)) )
    return lista
    
s= "123ABcdefZXYWE"  
s=s.lower()
s=''.join([i for i in s if not i.isdigit()])
