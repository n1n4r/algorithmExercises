#Escreva um programa que imprima os N primeiros números naturais ímpares. 
N = int(input("Informe N: "))
for i in range(1,N+1):
    if i%2 != 0:
        print(i, end=" ")