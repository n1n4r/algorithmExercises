#Uma  firma  contrata  um  encanador  a  R$  20,00  por  dia.  Escreva  um  programa  que  leia  o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% de imposto municipal.

workedDays = int(input("Informe a quantidade de dias trabalhados: "))
dailyRate = 20.00
localTax = 0.08
print(f"Para {workedDays} dias trabalhados o pagamento do encanador é R${(workedDays*dailyRate*(1-localTax)):.2f} e o imposto municial é R${(workedDays*dailyRate*localTax):.2f}")