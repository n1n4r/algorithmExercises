#Escreva um programa que lê um inteiro N e imprime os N primeiros inteiros negativos.
N=int(input("Informe o valor de N: "))
print(f"Os ",N," primeiros inteiros negativos são: ")
for i in range (N,0,-1):
    print("-",i,end=" ")
print("\n")