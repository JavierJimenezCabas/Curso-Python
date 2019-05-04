# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:08:53 2019

@author: Javier
"""
"""
print("Digite su Edad")
edad = input()
edad = int(edad)
if edad >= 18:
    print("Ya Eres Mayor de Edad")
else:
    print("Eres Menor de Edad")

print("Ya Eres Mayor de Edad") if edad >= 18 else print("Eres Menor de Edad")
"""

# Arrays
v1 = ["Hola", "Mundo", 3, 5, 6, 8, True, ["Otro", "Array", "Dentro"]]
v2 = ["Habla", "y", "Que"]
v3 = range(1, 5, 201)

# =============================================================================
# for x in v3:
# print(x)
# =============================================================================


print(v2[2])
v2.append("Javier")
v2.insert(0, "Hey")
# v2.clear()
v2.index("Habla")

print(v1[7][0])

print("Digite Numero Final")
numf = input()
numf = int(numf)
suma = numf*(numf+1)/2
print(suma)

vnum = range(0, numf+1)
x1 = 0
for x in vnum:
    x1 = x1 + x

i = 1
while i < 5:
    print(i)
    i = i + 1


# Funciones
def hola_mundo():
    print("Hola Mundo")


hola_mundo()


def elevar_cuadrado(numero=1):
    return numero ** 2


elevar_cuadrado(3.5)
