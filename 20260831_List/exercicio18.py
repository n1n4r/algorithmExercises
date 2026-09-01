#Uma companhia telefônica opera com a seguinte tarifa: uma chamada telefônica com duração de 3 minutos custa R$ 1,15. Cada minuto adicional custa R$ 0,26. Escreva um programa que leia a duração total de uma chamada (em minutos) e calcule o total a ser pago.

minutes = int(input("Informe a duração da chamada telefônica em minutos: "))
if minutes<=3:
    cost = minutes*1.15
else:
    cost = ((minutes-3)*0.26+3*1.15)
print(f"O custo da chamada telefônica é R${cost:.2f}")