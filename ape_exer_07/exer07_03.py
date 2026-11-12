#Escreva uma função desenhaQuadrado que exibe um quadrado sólido (o mesmo número de linhas e colunas). O caracter utilizando par preencher o quadrado e o valor do lado são passados como argumentos para a função. Por exemplo, se o caracter for x e o valor do lado for 5, a função deverá exibir
#xxxxx
#xxxxx
#xxxxx
#xxxxx
#xxxxx

ch=input("Informe o caractere: ")
n=int(input("Informe a quantidade de repetições: "))
def square(ch,n):
    for i in range(n):
        print(n*ch)
square(ch,n)