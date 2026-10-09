#Um quadrado perfeito é um número inteiro que resulta da multiplicação de um número inteiro por ele mesmo, possuindo assim uma raiz quadrada exata. Por exemplo, os números 1, 4, 9, 16 e 25 são quadrados perfeitos, mas os números 15 e 20 não são, pois não existe um número inteiro que multiplicado por si mesmo resulte em 15 ou 20. Escreva um programa que mostre os números quadrados perfeitos entre 100 e 200.
for i in range(100,201,1):
    n=i**(1/2)
    if n.is_integer():
        print(i, end=" ")
#-----
i=10
while i*i <= 200:
    print(i*i, end=" ")
    i = i+1
#-----
for i in range(100,201,1):
    n=int(i**(1/2))
    if n*n==i:
        print(i,end=" ")
