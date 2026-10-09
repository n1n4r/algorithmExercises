#Em uma empresa os funcionários renovam o  contrato por três  anos. O salário sofrerá um reajuste de 7%, 6% e 5%, respectivamente, nos próximos três anos. Escreva um programa  que leia o salário mensal atual do funcionário, e então, imprima o salário mensal para cada um dos três próximos anos.

salary = float(input("Informe o valor do seu salário antes do reajuste: "))
payRaise1 = 0.07
payRaise2 = 0.06
payRaise3 = 0.05
print(f"O funcionário que recebia salário de R${salary:.2f} passará a receber o salário de R${(salary*(1+payRaise1)):.2f} no primeiro ano, R$ {(salary*(1+payRaise1)*(1+payRaise2)):.2f} no segundo ano e R${(salary*(1+payRaise1)*(1+payRaise2)*(1+payRaise3)):.2f} no terceiro ano.")