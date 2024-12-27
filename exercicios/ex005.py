#Programa lê um valor e apresenta o seu valor sucessor e antecessor, base 10.

valor = int(input('Digite um número: '))

ante = valor - 1
suce = valor + 1

print(f"O sucessor do número {valor} é {suce}, e o antecessor é {ante}.")