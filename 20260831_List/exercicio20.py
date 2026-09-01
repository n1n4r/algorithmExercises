#Faça um programa que peça ao usuário os tamanhos dos catetos de um triângulo retângulo e mostre na tela o valor de sua hipotenusa.

from math import sqrt

leg1 = float(input("Informe o valor do primeiro cateto em centímetros: "))
leg2 = float(input("Informe o valor do segundo cateto em centímetros: "))
print(f"O valor da hipotenusa do triângulo retângulo de catetos {leg1:.2f}cm e {leg2:.2f}cm é {(sqrt((leg1**2)+(leg2**2))):.2f}cm")