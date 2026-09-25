#Escreva um programa que lê um número não determinado de valores para m, todos inteiros e positivos, um de cada vez. Se m for par, verificar quantos divisores possui e escrever esta informação. Se m for ímpar e menor do que 12 calcular e escrever o fatorial de m. Se m for ímpar e maior ou igual a 12 calcular e escrever a soma dos inteiros de 1 até m.
while True:
    m=int(input("Informe m: "))
    if m==0:
        break
    if m%2==0:
        #quantos divisores possui
        count=0
        for k in range(1,m//2+1):
            if m%k==0:
                count+=1
        print(f"{m} possui {count} divisores")
    elif m%2!=0 and m>12:
        #fatorial de m
        pass
    else:
        #soma dos inteiros ate m
        pass