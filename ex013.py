publicoTotal = int(input ('Digite o público total: '))
if publicoTotal <=0:
    print('por favor, digite um número valido!')

else:
    popular = (publicoTotal * 10/100) *10
    geral = (publicoTotal * 50/100) *50
    arquibancada = (publicoTotal * 30/100) *100
    cadeiras = (publicoTotal *10/100) *200
    print (f'O estádio irá arrecadar: R${popular+geral+arquibancada+cadeiras}')