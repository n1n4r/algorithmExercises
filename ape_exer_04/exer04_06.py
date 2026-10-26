#Escreva um programa que gere aleatoriamente um vetor de 20 elementos inteiros, menores do que 100. A seguir, conte e mostre quantos valores pares existem no vetor.
import random
vetor=[]
vetor_par=[]
n_par=0
for i in range(1,21):
    vetor.append(random.randint(1,100))
for item in vetor:
    if item%2==0:
        vetor_par.append(item)
        n_par=n_par+1
print(f"vetor randômico: {vetor}\nvetor com números pares: {vetor_par}\nquantidade de valores pares: {n_par}\n")