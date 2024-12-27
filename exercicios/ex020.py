#Programa randomiza uma lista de strings
from random import shuffle


nome = input('Digite um nome: ')
nome2 = input('Digite outro: ')
nome3 = input('Digite outro: ')
nome4 = input('Digite outro: ')

alunos = [nome, nome2, nome3, nome4]
shuffle(alunos)
print(alunos)