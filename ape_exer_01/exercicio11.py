#Faca um código que converta uma medida de temperatura de Fahrenheit (F) para Celsius (C). A  partir  da  fórmula  de  conversão  de  Celsius  para  Fahrenheit.  Deduza  a  fórmula  para  a conversão de Fahrenheit para Celsius para que você possa resolver o problema. C = (5/9).(F-32)

temp_F = float(input("Informe a temperatura em Fahrenheit(°F): "))
temp_C = (5/9)*(temp_F-32)
temp_test = ((9/5)*temp_C)+32
print(f"A temperatura de {temp_F:.2f}°F é igual a {temp_C:.2f}°C")
print(f"Isso quer dizer que {temp_C:.2f}°C é igual a {temp_test:.2f}°F")