#Programa lê quantia em reais e conversão para dólar.

valor = float(input('Digite um valor:'))
valord = valor * 0.1622

print(f'R${valor:.2f} equivalem á US${valord:.2f}')
