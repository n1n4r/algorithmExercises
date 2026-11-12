#Escreva um aplicativo completo para solicitar ao usuário o raio r de uma esfera, e calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize a seguinte fórmula para determinar o volume:
#𝑉 = (4/3)*pi()*r³
from math import pi
r = float(input("Informe o raio da esfera em centímetros: "))
def esphere(r):
    return (4/3)*pi*(r**3)
print (f"O volume da esfera é {esphere(r):.2f} cm²")