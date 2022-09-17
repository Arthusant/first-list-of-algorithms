morango = int(input('Quantidade em KG de morango: '))
maça = int(input('Quantidade em KG de maçã: '))

preço_morango = float(morango*2.50)
preço_maça = float(maça*1.80)

preço_morango2 = float( morango*2.20)
preço_maça2 = float (maça*1.50)

if morango <=5:
    print (f'Morango ficará por: R${preço_morango}')
if maça <=5:
    print (f'Maçã ficará por: R$ {preço_maça}')

elif morango >5 and morango <=8:
    print (f'{morango}KG de morango sairá por: R$: {preço_morango2}')
if maça >5 and maça <=8:
    print (f'{maça}KG de maçã sairá por: R$: {preço_maça2} ')

elif morango>8 or preço_morango2 >=25:
    print (f'O morango sairá por {((-preço_morango2*10)/100)+preço_morango2}')
if maça >8 or preço_maça2 >=25:
    print(f'A maçã sairá por {((-preço_maça2*10)/100)+preço_maça2}')