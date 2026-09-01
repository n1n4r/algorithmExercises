#Escreva um programa leia uma quantidade de tempo dada em horas, minutos e segundos e converta para um número equivalente em segundos. 
time = input("Informe as horas no formato 24h (HH:MM:SS): ")
hour = int(time[0:2])
minutes = int(time[3:5])
seconds = int(time[6:]) 
print(f"O tempo {time} possui {((hour*60*60)+(minutes*60)+(seconds))} segundos")