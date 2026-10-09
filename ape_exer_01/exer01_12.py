#Escreva  um  programa  que  a  partir  de  um  diâmetro  de  um  círculo  que  será  digitado  pelo usuário, calcular e exibir sua área. Area = pi().raio²

from math import pi
diameter = float(input("Informe o diâmetro do círculo em centímetros: "))
radius = diameter/2
area = pi*(radius**2)
print(f"A área do círculo de diâmetro {diameter:.2f}cm é {area:.2f}cm²")