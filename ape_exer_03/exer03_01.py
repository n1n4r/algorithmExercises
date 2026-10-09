#Escreva um programa que leia um texto pelo teclado e exiba-o na tela em ordem inversa.
#Exemplo: Para a string "Bom dia" a saída deve ser "aid moB". Não use o método reverse().

s=input("Informe uma frase: ")
print(s[::-1])
print("\n")
#-----
i=len(s)-1
while i>=0:
    print(s[i], end="")
    i=i-1
print("\n")