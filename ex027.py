venal = float(input('Qual o valor venal do carro? '))
tipo = input('qual o tipo do veiculo? (se automovel (1) \n se caminhote/furgão (2) \n se auto para transporte publico 3 \n se motocicleta (4) \n se veiculo de locadoras (5)'
             '\n se onibus caminhão ou trator (6): ')
if tipo == '1':
    print (f'Categoria de Automóveis:                         R${(venal*4)/100:.3f}')

elif tipo == '2':
    print (f'Categoria de Caminhotes de Carga e Furgão:       R${(venal*3)/100:.3f}')

elif tipo == '3':
    print (f'Categoria de Automóveis para Transporte Público: R${(venal*2)/100:.3f}')

elif tipo == '4':
    print (f'Categoria de Motocicletas:                       R${(venal*2)/100:.3f}')

elif tipo == '5':
    print (f'Categoria de Veiculos Locadores:                 R${(venal*1)/100:.3f}')

elif tipo == '6':
    print (f'Categoria de Ônibus, Caminhão e Trator:          R${(venal*1)/100:.3f}')

else:
    print ('por favor, digite um valor presente na tabela acima')