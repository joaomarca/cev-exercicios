#Programa lê uma temperatura em C° e converte em F° e K°

temp = float(input('Digite a temperatura em C°: '))
tempF = (temp * 9/5) + 32
tempK = temp + 273.15

print(f'{temp} equivale á {tempF}F° e {tempK}K°.')