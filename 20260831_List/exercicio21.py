"""
No país de Brasilândia a moeda nacional é a merreca (M$). Sabe-se que o sistema monetário de Brasilândia só utiliza moedas, não utiliza cédulas, e que os valores dos diferentes tipos de moeda são os seguintes:
Valor (M$)  Descrição 
1,00  Moeda de uma merreca 
5,00  Moeda de cinco merrecas 
10,00  Moeda de dez merrecas 
50,00  Moeda de cinquenta merrecas 
100,00  Moeda de cem merrecas
Devido  ao  acúmulo  de  moedas  por  parte  dos  brasilândios,  o  Governo  resolveu  abrir  uma concorrência  internacional  para  o  desenvolvimento  de  um  software.  Dado  um  valor  em merreca,  o  programa  deve  calcular  qual  o  número  mínimo  de  moedas  necessárias  para perfazer o valor especificado.
Exemplo: Se o valor for M$ 187,00, a saída de programa deve ser: 
1 moeda(s) de M$ 100,00 
1 moeda(s) de M$ 50,00 
3 moeda(s) de M$ 10,00 
1 moeda(s) de M$ 5,00 
2 moeda(s) de M$ 1,00 
"""
value = float(input("Informe um valor de merreca: "))

coin100 = 0
change100 = 0
coin50 = 0
change50 = 0
coin10 = 0
change10 = 0
coin05 = 0
change05 = 0
coin01 = 0

if value>=100:
    coin100 = (value - (value%100))/100
    change100 = value - coin100*100
else:
    change100 = value

if change100>=50:
    coin50 = (change100 - (change100%50))/50
    change50 = change100 - coin50*50
else:
    change50 = change100

if change50>=10:
    coin10 = (change50 - (change50%10))/10
    change10 = change50 - coin10*10
else:
    change10 = change50

if change10>=5:
    coin05 = (change10 - (change10%5))/5
    change05 = change10 - coin05*5
else:
    change05 = change10

if change05>=1:
    coin01 = change05
else:
    print("ERRO!!!")

print(f"A quantidade mínima de moedas para M${value:.2f} é:")
print(f"{coin100:g} moeda de 100, {coin50:g} moeda de 50, {coin10:g} moeda de 10, {coin05:g} moeda de 5 e {coin01:g} moeda de 1")
