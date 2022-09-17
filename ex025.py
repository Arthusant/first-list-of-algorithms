idade = int(input('Qual a idade do nadador? '))
if idade >=5 and idade <=7:
    print ('O nadador faz parte da categoria: Infantil A!')

elif idade >=8 and idade <=10:
    print ('O nadador faz parte da categoria: Infantil B!')

elif idade >=11 and idade <=13:
    print ('O nadador faz parte da categoria: Juvenil A!')

elif idade >=14 and idade <=17:
    print ('O nadador faz parte da categoria: Juvenil B!')

elif idade >=18:
    print ('Esse nadador faz parte da categoria dos Adultos!')

else:
    print ('Pfv digite uma idade válida. \n ---Fim---')