colaborador = float(input ('Qual o salario desse colaborador? '))

if colaborador <=280:
    print (f'O salário antes do reajuste era de: {colaborador}')
    print (f' O percentual de aumento será de 10%')
    print (f'O valor do aumento foi de {(colaborador*10)/100}')
    print (f' O salário desse colaborador ficará ${(colaborador*0.10) + colaborador}')

elif colaborador >280 and colaborador <=699:
    print (f'O salário antes do reajuste era de: {colaborador}')
    print (f'O percentual de aumento foi de 15%')
    print (f'O valor do aumento foi de {(colaborador*15)/100}')
    print(f'O salário final desse colaborador será de ${(colaborador*0.15)+colaborador}')

elif colaborador >700 and colaborador <=1499:
    print (f'O salário antes do reajuste era de: {colaborador}')
    print (f'O percentual de aumento foi de 10%')
    print (f'O valor do aumento foi de {(colaborador*10)/100}')
    print (f'O salário desse colaborador será de ${(colaborador*0.10) + colaborador}')

else:
    print (f'O salário antes do reajuste era de: {colaborador}')
    print (f'O percentual de aumento será de 5%')
    print (f'O valor do aumento foi de {(colaborador*5)/100}')
    print (f'O valor desse colaborador será de ${(colaborador*0.05) + colaborador}')