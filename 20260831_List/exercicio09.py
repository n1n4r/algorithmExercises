#Escreva um programa para calcular e exibir o volume de um cone a partir dos valores da altura e do raio da base que serão digitados pelo usuário. Volume = (1/3).pi().raio².altura 

radius = int(input("Informe o raio: "))
height = int(input("Informe a altura: "))
volume = (1/3) * 3.14 * (radius ** 2) * height
print(f"O volume do cone é {volume}")