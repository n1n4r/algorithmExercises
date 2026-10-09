"""
C. Exchange Rate
time limit per test
1 second
memory limit per test
1024 megabytes

Robertinho has been considering buying another keyboard, one of his favorite objects. Since he is going to travel abroad and knows that some products can cost much less outside the country, he wants help deciding whether it is worth buying the new keyboard there.

In Brazil, where he lives, the keyboard costs C reais, the local currency. In Nlogônia, the country he will visit, the same keyboard costs K nlogarian dollars. Given that the exchange rate is T reais per nlogarian dollar, after conversion, the cost of the purchase abroad is equivalent to KxT reais.

Given the information about the current exchange rate T, the cost in Brazil C, and the cost abroad K, determine the smallest amount (in reais) that Robertinho can pay for the product.
Input

The input consists of a single line containing three integers T, C, and K (1≤T,C,K≤1000), representing, respectively, the exchange rate, the price of the product in Brazil, and the price of the product abroad in the foreign currency.
Output

Print a single line containing an integer: the smallest amount in reais that Robertinho can pay for the product.
"""

exchangeRate = int(input("Informe a taxa de câmbio (reais x nlogorian dollar): "))
reais = int(input("Informe o dinheiro que você tem em Reais(R$): "))
nlogonia = int(input("Preço do teclado em nlogorian dollar: "))

if reais>=(exchangeRate*nlogonia):
    print(exchangeRate*nlogonia)
else:
    print(reais)