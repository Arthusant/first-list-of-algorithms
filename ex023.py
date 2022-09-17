saque = int(input('Quanto você quer sacar? R$'))
total = saque
cedula = 100
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        print (f'total de {totalCedula} cédulas de R${cedula}')
        if cedula ==100:
            cedula = 50
        elif cedula ==50:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        if total == 0:
            break