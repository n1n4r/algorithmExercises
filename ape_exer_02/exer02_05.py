#Escreva um programa que lê um inteiro N e uma sequência de N números inteiros, e imprime a soma dos números pares da sequência lida.
N = int(input("Informe o valor de N: "))
soma = 0
print(f"Os numeros pares na sequência de números inteiros em ",N," são:")
for i in range (1,N+1):
    if i%2 == 0:
        soma = soma + i
        print(i, end=" ")
print(f"\nA soma desses números é: ", soma)
print("\n")