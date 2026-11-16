#Fazer um programa para obter três notas e calcular e exibir a sua média, usando uma função para o cálculo da média.

score1 = int(input("Informe a primeira nota: "))
score2 = int(input("Informe a segunda nota: "))
score3 = int(input("Informe a terceira nota: "))

def GPA (s1,s2,s3):
    print(f"A média das notas é: {((s1+s2+s3)/3):.2f}")

GPA(score1,score2,score3)