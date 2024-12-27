#Programa lê um número e imprime seu dobro, seu triplo e sua raiz quadrada.
from math import sqrt

valor = float(input('Digite um número: '))

dobro = valor * 2
triplo = valor * 3
raiz = sqrt(valor)

if raiz % 2 == 0:
    raiz = int(raiz)
    
print(f'O dobro de {valor} é {dobro}, o triplo é {triplo} e sua raíz quadrada é {raiz}.')