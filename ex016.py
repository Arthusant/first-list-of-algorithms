numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))
if numero1 > numero2 and numero1 > numero3:
    print (f'O primeiro número é o maior: {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print (f'O segundo número é o maior: {numero2}')
elif numero3 > numero1 and numero3 > numero2:
    print (f'O terceiro numero é o meior: {numero3}')