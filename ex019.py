hora = int(input('Horas trabalhadas: '))
dinheiro = float(input('Quanto você recebe por hora? '))
salario_bruto = hora*dinheiro

sindicato = (salario_bruto*3)/100
fgts = (salario_bruto*11)/100

if salario_bruto <=0:
    print('por favor digite um valor valido!')

elif salario_bruto <=900:
     print (f'Salário bruto: horas trabalhadas: {hora} ganho por hora: {dinheiro} : R$ {salario_bruto}')
     print (f'(-) IR (isento)                                                     : R$ 00:00')
     print (f'(-) Sindicato(-3%)                                                  : R${sindicato}')
     print (f'FGTS (-11%)                                                         : R${fgts}')
     print (f'O salário com os descontos ficará por                               : R${salario_bruto - sindicato }')

elif salario_bruto >900 and salario_bruto <=1500:
    ir = (salario_bruto*5)/100
    print(f'Salário bruto: horas trabalhadas: {hora} ganho por hora: {dinheiro} : R$ {salario_bruto}')
    print(f'(-) IR (5%)                                                         : R$ {ir}')
    print(f'(-) Sindicato(-3%)                                                  : R$ {sindicato}')
    print(f'FGTS (-11%)                                                         : R$ {fgts}')
    print(f'O salário com os descontos ficará por                               : R$ {salario_bruto - ir - sindicato}')

elif salario_bruto >1500 and salario_bruto <=2500:
    ir = (salario_bruto*10)/100
    print(f'Salário bruto: horas trabalhadas: {hora} ganho por hora: {dinheiro} : R$ {salario_bruto}')
    print(f'(-) IR (10%)                                                        : R$ {ir}')
    print(f'(-) Sindicato(-3%)                                                  : R$ {sindicato}')
    print(f'FGTS (-11%)                                                         : R$ {fgts}')
    print(f'O salário com os descontos ficará por                               : R$ {salario_bruto - ir - sindicato}')

elif salario_bruto >2500:
    ir = (salario_bruto*20)/100
    print(f'Salário bruto: horas trabalhadas: {hora} ganho por hora: {dinheiro} : R$ {salario_bruto}')
    print(f'(-) IR (20%)                                                        : R$ {ir}')
    print(f'(-) Sindicato(-3%)                                                  : R$ {sindicato}')
    print(f'FGTS (-11%)                                                         : R$ {fgts}')
    print(f'O salário com os descontos ficará por                               : R$ {salario_bruto - ir - sindicato}')