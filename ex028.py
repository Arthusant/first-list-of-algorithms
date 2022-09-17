capacidade = float(input('Qual a capacidade do elevador (em T)? '))
capacidade2 = capacidade * 1000
pessoas = float(input('Qual o peso total de pessoas (em KG)? '))
resultado = capacidade2 - pessoas
if resultado >=0:
    print ('Não excedeu a carga, pode subir! :D')
else:
    print ('Infelizmente excedeu a carga do elevador! :(')
