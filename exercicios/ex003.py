#Programa pede dois valores e apresenta a soma desses valores.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n = n1 + n2

#Duas possibilidades, uma é mais curta e efetiva.

#print('A soma de {} e {} vale {}'.format(n1, n2, n))
print(f'A soma de {n1} e {n2} é: {n}')