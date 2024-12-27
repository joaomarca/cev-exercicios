#Programa lê um ângulo e devolve o valor do seno, cosseno e tangente.
from math import sin, cos, tan, radians

ang = float(input('Digite o valor do ângulo: '))

print(f'O ângulo {ang} representa o seno de {sin(radians(ang)):.2f}, o cosseno de {cos(radians(ang)):.2f} e a tangente de {tan(radians(ang)):.2f}')