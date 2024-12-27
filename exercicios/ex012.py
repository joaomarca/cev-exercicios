#Programa lê o preço do produto e devolve o preço com desconto.

valor = float(input('Digite o preço em reais: '))

desconto = int(input('Digite a porcentagem do desconto: '))

valordesconto = valor - (valor * desconto / 100)

print(f'O preço de R${valor:.2f} com um desconto de {desconto}% fica com um preço de R${valordesconto:.2f}')