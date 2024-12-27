#Programa1 pede um input e apresenta diversas características desse input.
#Programa2 pede dois valores e realiza diversas expressões aritméticas com os dois valores.

algo = input("Digite algo: ")
print(f"{algo} é {type(algo)}")

if algo.isnumeric():
    print(f'{algo} é numerico.')
if algo.isalpha():
    print(f'{algo} é alfabetico.')
if algo.isalnum():
    print(f'{algo} é alfanumerico.')
if algo.isdecimal():
    print(f'{algo} é decimal.')
if type(algo) == str:
    print('oii')

algo2 = float(input('Digite um numero: '))
algo21 = float(input('Digite outro: '))
soma = algo2 + algo21
multi = algo2 * algo21
div = algo2 / algo21
divint = algo2 // algo21
expo = algo2 ** algo21

print(f'A soma de {algo2} e {algo21} é {soma}. A multiplicação é {multi}, a divisão é {div},', end=' ')

#End faz o próximo print começar na mesma linha, o \n quebra a linha onde foi colocado.

print(f'a divisão inteira é {divint}.\nA exponenciação é {expo}.')