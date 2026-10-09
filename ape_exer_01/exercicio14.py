#Escreva um programa para calcular e exibir a tensão V depois que o usuário inserir o valor da resistência R e da corrente i. V = R . i

resistance = float(input("Informe o valor da resistência em ohm (Ω): "))
current = float(input("Informe o valor da corrente em ampere (A): "))
print(f"Para uma corrente de {current:.2f}A e resistência {resistance:.2f}Ω a tensão resultante é {(current*resistance):.2f}V")