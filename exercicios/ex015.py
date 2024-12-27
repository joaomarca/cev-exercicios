#Programa lê os km rodados de um carro alugado e a quantia de dias alugados, calculando o preço a se pagar.

km = float(input('Quantos km o carro rodou? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

#R$60 por dia alugado e R$0.15 por quilômetro rodado

preco = (km * 0.15) + (dias * 60)

print(f'O preço a se pagar na devolução do carro é de R${preco:.2f}.')