ano = int(input('Digite um número correspondente a um ano: '))
if (ano % 4 == 0 and ano %100 !=0):
    print (f'O ano {ano} é bissexto!')
elif (ano%400==0):
    print (f'O ano {ano} é bissexto!')
else:
    print (f'O ano {ano} não é bissexto!')
