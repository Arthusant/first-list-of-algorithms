mb = int(input('Qual o tamanho do arquivo em MB? '))
mbps = int(input('Qual a velocidade da sua internet em MBps? '))
print (f'O tempo de download será {(mb/(mbps/8))/60:.2f}')
