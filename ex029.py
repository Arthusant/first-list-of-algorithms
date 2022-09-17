conta = int(input('Qual o número da conta do cliente? '))
consumo = float(input('Qual o consumo de água por metros cúbicos? '))
consumidor = input('Qual o tipo de consumidor? ')

residencial = 50 + (0.5*consumo)
comercial = (0.25*(consumo-80))+500
industrial = (0.04*(consumo-100)) + 800

if consumidor !=comercial and industrial:
    print (f'O cliente {conta}, terá que pagar: R${residencial}')

elif consumidor !=residencial and industrial:
    print (f"O ..cliente {conta}, terá que pagar: R${comercial}")

elif consumidor !=residencial and comercial:
    print (f'O cliente {conta}, terá que pagar: R${industrial}')