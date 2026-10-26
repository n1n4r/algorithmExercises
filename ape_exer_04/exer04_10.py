# Escreva um programa que leia um vetor de números inteiros com 30 posições e crie um segundo vetor, substituindo todos os valores ímpares por 0. Mostre os 2 vetores.
import random
vetor=[]
vetor2=[]
for i in range(1,31):
    vetor.append(random.randint(1,999))
for item in vetor:
    if item%2!=0:
        item = 0
        vetor2.append(item)
    else:
        vetor2.append(item)
print(f"vetor inicial: {vetor}\nvetor modificado: {vetor2}\n")
