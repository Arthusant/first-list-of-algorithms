hora = int('Horas trabalhadas: ')
dinheiro = float('Quanto você recebe por hora? ')
salario_bruto = hora*dinheiro

 if salario_bruto <=900:
     print (f'Salário bruto: horas trabalhadas: {hora} ganho por hora: {dinheiro} : R$ {salario_bruto}')
     print (f'(-) IR (isento)                                                     : R$ 00:00')
     print (f'(-) INSS (-  %)                                                     : R$      ')
