#Escreva um programa que leia três números de ponto flutuante e imprima a média aritmética entre eles.

value1 = float(input("Informe o primeiro valor :"))
value2 = float(input("Informe o segundo valor: "))
value3 = float(input("Informe o terceiro valor: "))
average = (value1 + value2 + value3)/3
print(f"A média de {value1}, {value2} e {value3} é {average}")