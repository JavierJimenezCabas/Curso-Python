# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:08:53 2019

@author: Javier
"""

print("Digite su Edad")
edad = input()
edad = int(edad)
if edad >= 18:
    print("Ya Eres Mayor de Edad")
else:
    print("Eres Menor de Edad")

print("Ya Eres Mayor de Edad") if edad >= 18 else print("Eres Menor de Edad")
