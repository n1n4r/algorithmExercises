# Escreva um programa que leia um valor real (float) e exiba-o na tela com milhares separados por ponto ('.') e as casas decimais separadas por vírgula (','). Por exemplo, para o número 8387932.701 o programa deve exibir "8.387.932,701".

number = 8387932.701
number_int = int(number)
number_dec = number%1
string_int = str(number_int)
i = len(string_int)-1
j=1
string_s = ""
while i >= 0:
#    if j%3==0:
#        string_s = "." + string_int[i] + string_s
#        j=j+1
#        i=i-1
#    else:
#        string_s = string_int[i] + string_s
#        j=j+1
#        i=i-1
    string_s = string_int[i] + string_s
    if j%3==0:
        string_s = "." + string_s
    j=j+1
    i=i-1
string_dec = str(number_dec)
string_dec = string_dec[2:5]
print(f"{string_s},{string_dec}")