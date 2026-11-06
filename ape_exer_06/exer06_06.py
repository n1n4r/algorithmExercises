#Faça um programa que leia nomes de alunos e suas respectivas notas até que o nome ’oooo’ seja informado, após o fim da leitura, imprima o nome do aluno que possui a maior nota. Obs.: Use dicionário para resolver essa questão.

students = {"Raimundinha":7.80,"Jorgim":8.70,"Maricleusa":3.70,"Paolla":6.50,"Astrogildo":9.20}
biggest_key = ""
biggest_value = 0
for key in students:
    actual_value = students[key]
    if actual_value > biggest_value:
        biggest_value = actual_value
        biggest_key = key

print(f"{key} é o aluno com maior nota que é igual a {biggest_value}")

#---
dic={}
while True:
    nome = input("Informe o nome: ")
    if nome == "ooo":
        break
    nota = float(input("Informe a nota: "))
    dic[nome]=nota
maior = 0.0
aluno = ""
for nome in dic:
    if dic[nome]>maior:
        maior = dic[nome]
        aluno = nome
print (f"Maior nota - {aluno}: {maior} ")


