#Escreva um programa para calcular e exibir a área de um quadrado a partir do valor de sua diagonal que será informado pelo usuário.

diagonal = float(input("Informe a diagonal do quadrado em centímetros: "))
# diagonal² = 2 side² => diagonal = side x (2^(1/2)) => side = diagonal / (2^(1/2))
area = (diagonal/(2**(1/2)))**2
print(f"A área do quadrado de diagonal {diagonal:.2f}cm é {area:.2f}cm²")
