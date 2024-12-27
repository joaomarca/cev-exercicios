#Programa sorteia 1 nome de uma lista de 4
from random import choice


nome = input('Digite um nome: ')
nome2 = input('Digite outro: ')
nome3 = input('Digite outro: ')
nome4 = input('Digite outro: ')

lista = [nome, nome2, nome3, nome4]

print(choice(lista))