# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 0
print ("")
podstawa = int(input("Podstawa(2-35)?: "))
podstwyj = int(input("Podstawa docelowa(2-35)?: "))
print("Podaj kolejne cyfry liczby w systemie 10, cyfra>podstawa aby zakonczyc")
cyfra = 0
while (cyfra<podstawa):
    x = x*podstawa + cyfra
    cyfra = int(input(" "))
    
print("Wynik(10) to: ",x)
print("Wynik(",podstwyj,") to: ",end="")
lista = []
while (x>0):
    lista.append(x%podstwyj)
    x =x//podstwyj
#lista.reverse
for i in list(reversed(lista)):
    print(i,end=" ")    










