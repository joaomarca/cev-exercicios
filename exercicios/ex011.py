#Programa lê altura e largura de uma parede em metros, calcula a área e a quantia de tinta necessária para pintar ela, tendo que cada litro de tinta pinta 2m²

alt = float(input('Digite a altura: '))
larg = float(input('Digite a largura: '))

area = alt*larg

tinta = area / 2

print(f'Essa parede mede {area}m² e necessita de {tinta} litros de tinta para ser pintada.')