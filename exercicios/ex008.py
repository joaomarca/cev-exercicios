#Programa lê um valor em metros e converte em centímetros e milímetros.

valorm = float(input('Digite o valor em metros: '))
valorcm = valorm * 100
valormm = valorcm * 10

if valorm>1:
    print(f'{valorm} metros tem {valorcm} centímetros e {valormm} milímetros')
else:
    print(f'{valorm} metro tem {valorcm} centímetros e {valormm} milímetros')