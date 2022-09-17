altura = float(input('Qual a sua altura? '))
sexo = (input('Qual o seu sexo (homem\mulher)? '))

homem = (72.7*altura) - 51
mulher = (62.1*altura) - 44.7

if homem:
    print (f'seu peso ideal é: {homem}')

elif mulher:
    print (f'Seu peso ideal é: {mulher}')