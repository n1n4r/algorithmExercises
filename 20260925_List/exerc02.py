#Escreva um programa que leia um texto pelo teclado e exiba este texto em letras maiúsculas.

s=input("Informe uma frase: ")
print(f"{s.upper()}")
print("\n")

#-----
# codigo=ord("A")
# print(codigo)
# letra=chr(65)
# print(letra)

i=0
txt=""
while i < len(s):
    if ord(s[i])>=97 and ord(s[i])<=122:
        txt = txt + chr(ord(s[i])-32)
    else:
        txt = txt + s[i]
    i=i+1
print(txt)