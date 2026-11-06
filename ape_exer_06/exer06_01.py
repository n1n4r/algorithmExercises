# Escreva uma função, chamada contaVoigais, que conta todas as vogais presentes no texto recebido como parâmetro e retorna um dicionário contendo a quantidade de cada vogal.
# Escreva um programa a fim de testar sua função, e exiba, no fim, os dados do dicionário retornado.

texto = input("Informe uma frase para contar as vogais: ")
dic = {'a':0,'e':0,'i':0,'o':0,'u':0}

print(dic)

for letra in texto:
    if letra == 'a' or letra =='A':
        dic['a'] += 1
    if letra == 'e' or letra =='E':
            dic['e'] += 1
    if letra == 'i' or letra =='I':
            dic['i'] += 1
    if letra == 'o' or letra =='O':
            dic['o'] += 1
    if letra == 'u' or letra =='U':
            dic['u'] += 1

print(dic)