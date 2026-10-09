#Escreva um programa para converter de dólar para real e exibir para o usuário a resposta final. 

dolar = float(input("Informe o valor em dólar: "))
exRate = float (input("Informe a cotação do dólar: "))
#exRate = 5.17
reais = dolar * exRate
print(f"O valor de ${dolar} é R${reais}")