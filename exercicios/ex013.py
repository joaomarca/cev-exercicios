#Programa lê o salário de um funcionário e devolve seu salário com aumento.

valor = float(input('Digite o valor do salário em reais: '))
aumento = float(input('Digite o valor do aumento em porcentagem: '))
valoraumento = valor + (valor * aumento / 100)
print(f'O salário de R${valor:.2f} com um aumento de {aumento}% vai para R${round(valoraumento):.2f}')