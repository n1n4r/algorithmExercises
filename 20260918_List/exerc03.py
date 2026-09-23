#Escreva um programa que lê um inteiro N e imprime a soma dos N primeiros números inteiros.
N = int(input("Informe N: "))
soma = 0
for i in range(N+1):
    soma = soma + i
print(f"A soma dos numeros inteiros até", N, "é igua a", soma)

