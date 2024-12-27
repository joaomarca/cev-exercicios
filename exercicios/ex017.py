#Programa lê o comprimento de um cateto oposto e adjacente de um triângulo retângulo e retorne o valor da hipotenusa
from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))

ca = float(input('Digite o comprimento do cateto adjacente: '))

print(f'O comprimento da hipotenusa desse triângulo é de {hypot(co, ca)}')