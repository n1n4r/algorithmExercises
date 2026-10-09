# Escreva um programa que gere aleatoriamente um vetor de 50 posições de números inteiros e mostre-o na tela na ordem normal e depois na ordem inversa. Não use o método reverse()
import random
vetor=[]
for i in range (1,51):
    n=random.randint(1,100)
    vetor.append(n)
for item in vetor:
    print(item, end=" ")
print("\n")
i=len(vetor)-1
while i>=0:
    print(vetor[i],end=" ")
    i=i-1
print("\n")