x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

if x>0 and y>0:
    print ('Nesse caso faz parte do 1° Quadrante!')

elif x<0 and y>0:
    print ('Nesse caso faz parte do 2° Quadrante!')

elif x<0 and y<0:
    print ('Nesse caso faz parte do 3° Quadrante!')

elif x>0 and y<0:
    print ('Nesse caso faz parte do 4° Quadrante!')

else:
    print ('Por favor digite um valor diferente de 0!')