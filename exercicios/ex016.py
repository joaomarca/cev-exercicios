#Programa lê um número inteiro ou flutuante e retorna apenas a parte inteira do número
from math import trunc

valor = float(input('Digite um número: '))
print(f'A parte inteira de {valor} é {trunc(valor)}')