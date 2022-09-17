ladoA = int(input ('Primeiro lado do triangulo:  '))
ladoB = int(input ('Segundo lado do triangulo: '))
ladoC = int(input ('Terceiro lado do triangulo: '))

if (ladoA + ladoB < ladoC) or (ladoA + ladoC < ladoB) or (ladoB + ladoC < ladoA):
    print ('Não é um triangulo!')

elif (ladoA == ladoB) and (ladoA == ladoC):
    print('Equilatero, pois tem três lados iguais!')

elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
    print('Isósceles, pois tem apenas 2 lados iguais')

else:
    print('Escaleno, os 3 lados são diferentes')
