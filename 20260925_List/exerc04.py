#Escreva um programa que lê uma string S e inteiros não-negativos I e J e imprima o segmento S[I..J]. Não use slice (fatiamento).

S = input("Informe uma frase: ")
i = int(input("Informe o primeiro indice: "))
j = int(input("Informe o ultimo indice: "))

print(f"{S[i:j+1]}")