# -*- coding: utf-8 -*-
"""
Comentario
de parrafo
"""
import math
import numpy

# Hola Mundo
print("Hola Mundo")

# Variables
x = 5  # Int
y = "Texto"  # String
z = 4.5  # Float
a = True  # Bool
b = False  # Bool
c = 4+5j  # Complejo

print(x, y, z, a, b, c)

# Conocer el tipo de dato
print(type(b))

# Enteros
x = int(2)
print(x)
x = int("3")
print(x)

# Float
x = float(2)
print(x)
x = float(2.5)
print(x)
x = float("2")
print(x)
x = float("2.5")
print(x)

# string
x = str(2)
print(x)
y = str("3")
print(x)
z = str("2")
print(x)

# Manejo de cadenas de texto y algunos métodos
cad = "Hello World"
print(cad[0:5])  # Notoma el último valor

cad = "   Hello World   "
print(cad[0:5])
cad = cad.strip()
print(cad)

cad = "Hello World"
print(len(cad))
print(cad.lower())
print(cad.upper())

print(cad.replace('l', 'Y'))
print(cad.split(' '))
print(cad.split('l'))

# Operaciones

# Operaciones Aritméticas
a = 2
b = 3
c = a+b
c = a-b
c = a*b
c = a/b
c = a**b  # a^b
c = math.sqrt(a)
A = [[1, 2, 3, 6], [7, 8, 9, 10]]

# Captura por consola
print("Digite Nombre")
nombre = input()
print("Hola "+nombre+"...")

print("Digite el primer numero")
n1 = input()
n1 = float(n1)
print("Digite el segundo numero")
n2 = input()
n2 = float(n2)
print(n1+n2)

# Condiciones
a = 6
b = 5
if a > b:
    print(a, "es mayor que ", b)
else:
    print(b, "es mayor que ", a)
if a < b:
    if b > 1:
        print(b, "es mayor que 1 y es mayor que ", a)

if a == b:
    print("Son iguales")
elif a > b:
    print(a, "es mayor que ", b)
else:
    print(b, "es mayor que ", a)

a = 3
b = 3
if a == b and a > 2:
    print(a, "es igual a ", b, "mayor que 2")

if a == b or a > 2:
    print(a, "es igual a ", b, "mayor que 2")













