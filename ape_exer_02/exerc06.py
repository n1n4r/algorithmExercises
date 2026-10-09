#Produza duas versões de um programa que escreva n ≥ 0 asteriscos em uma linha sendo o valor n fornecido pelo usuário. A primeira versão deve utilizar o comando for e a segunda o comando while. Compare as duas versões. 
n = int(input("Informe o valor de n: "))
for i in range (n):
    print("*", end=" ")
print(" \n")

while n>0:
    print("*", end=" ")
    n = n-1
print(" \n")