nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if media >=7 and media!=10:
    print ('Aprovado!')
else:
    if media<7:
        print ('Reprovado')
    else:
        print ('aprovado com distinção!')