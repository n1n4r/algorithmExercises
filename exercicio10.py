#Escreva um programa que leia a altura e o raio de um cilindro circular e imprima o volume do mesmo. Obs: Imprima o volume com uma precisão de duas casas decimais. Volume = pi().raio².altura

from math import pi
height = float(input("Informe a altura do cilindro em centímetros: "))
radius = float(input("Informe o raio do cilindro em centímetros: "))
volume = pi*(radius**2)*height
print(f"O volume do cilindro de altura de {height:.2f}cm e raio de {radius:.2f}cm é {volume:.2E}cm²")