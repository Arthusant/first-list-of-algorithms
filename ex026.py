altura = float(input('Qual a sua altura? '))

if altura <=0:
    print ('Digite uma altura válida')

else:
    sexo = (input('Qual o seu sexo (homem\mulher)? '))

    homem = (72.7*altura) - 51
    mulher = (62.1*altura) - 44.7

    if sexo == "homem":
        print (f'seu peso ideal é: {homem:.2f}')

    elif sexo == "mulher":
        print (f'Seu peso ideal é: {mulher:.2f}')

    else:
        print ('por favor, digite um valor válido!')