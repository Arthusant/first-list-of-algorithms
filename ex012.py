hora = int(input('Número de horas trabalhadas? '))
din = float(input('Ganho por hora trabalhada: '))
bruto = (hora*din)
print (f'O salário bruto é {bruto}')
print (f'o desconto do IR ficará {bruto - (bruto*11/100)}')
print (f'o desconto do INSS ficará {bruto - (bruto*8/100)}')
print (f'o desconto do Sindicato ficará {bruto - (bruto*5/100)}')
ir = bruto*11/100
inss = bruto*8/100
sindicato = bruto*5/100
print (bruto - ir - inss - sindicato)
