# Criar uma função que converta graus para radianos e outra função que converta de radianos para graus. Fazer um aplicativo que testa as funções.

radiandos = float(input("Informe um valor em radiandos: "))
graus = float(input("Informe um valor em graus: "))

from math import pi

def rad(grau):
    return (grau*(pi/180))

def grau(rad):
    return (rad*(180/pi))

print(f"O valor de {radiandos:.2f} radiandos em graus é {grau(radiandos):.2f} graus")
print(f"O valor de {graus:.2f} graus em radiandos é {rad(graus):.2f} radiandos")
