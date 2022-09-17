sacos = int(input('Quantos sacos de raçao?' ))
KGsaco = float(input('Quantos KG em cada saco? '))
kg = sacos*KGsaco
gramas = kg * 1000
grupoAve = gramas/2
print (f'Cada grupo de ave receberá: {grupoAve} Gramas de ração!')
print (f'Após uma semana restará {gramas%7} Gramas!')