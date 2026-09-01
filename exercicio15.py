"""Escrever um programa que leia três valores reais A, B e C e calcule: 
a) a área do triângulo que tem A por base e B por altura. 
b) a área do círculo de raio C. 
c)  a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado de lado B. 
e) a área do retângulo de lados A e B."""

from math import pi
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))
print(f"A área do triângulo de base A: {a:.2f} e altura B: {b:.2f} é {((a*b)/2):.2f}")
print(f"A área do círculo de raio C: {c:.2f} é {(pi*(c**2)):.2f}")
print(f"A área do trapézio que tem bases A: {a:.2f} e B: {b:.2f} e altura C: {c:.2f} é {(((a+b)*c)/2):.2f}")
print(f"A área do quadrado de lado B: {b:.2f} é {(b*b):.2f}")
print(f"A área do retângulo de lados A: {a:.2f} e B: {b:.2f} é {(a*b):.2f}")