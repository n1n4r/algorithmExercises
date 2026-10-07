# Escreva um programa que leia um texto pelo teclado e exiba este texto com as primeiras letras de cada palavra em maiúsculas. (Nota: Uma palavra é qualquer sequência de caracteres separada por um ou mais espaços).

s=input("Informe uma frase: ")
print(f"{s.title()}")

#-----
#ASCII do espaço = 32
#ASCII A a Z = 65 a 90
#ASCII a a z = 97 a 122

i=0
txt=""
while i < len(s):
    if s[i]==0:
        txt = txt + chr(ord(s[i])-32)
    elif ord(s[i])==32:
        txt = txt + chr(ord(s[i+1])-32)
    else:
        txt = txt + s[i]
    i=i+1
print(txt)