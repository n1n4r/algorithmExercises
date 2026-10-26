#Faça um programa que leia um código numérico inteiro e um vetor de 30 posições de números reais. Se o código for zero, termine o programa. Se o código for 1, mostre o vetor na ordem direta. Se o código for 2, mostre o vetor na ordem inversa (não use o método reverse). Se o código for 3, calcule e mostre a média aritmética dos itens do vetor
import random
n=int(input("Informe o codigo 1, 2 ou 3: "))
vetor=[]
for i in range(1,11):
    vetor.append(round(random.uniform(-999.0,999.0),3))
for item in vetor:
    if n==1:
        print(f"vetor ordem direta: {vetor}\n")
    elif n==2:
        i=len(vetor)-1
        while i>=0:
            print(vetor[i],end=" ")
            i=i-1
    else:
        print(f"vetor ordem ???: {vetor}\n")
print(vetor)
#print(f"vetor inicial: {vetor}\nvetor modificado: {vetor2}\n")