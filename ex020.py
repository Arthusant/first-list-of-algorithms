nota1 = float(input(f'Qual foi a primeira nota do aluno? '))
nota2 = float(input(f'Qual foi a segunda nota do aluno? '))
media = (nota1 + nota2)/2

if media <=4.0 and media >=0:
    print (f'Conceito: E, suas notas foram {nota1, nota2} a media ficou {media}, REPROVADO :(')

elif media >4.0 and media <6.0:
    print (f'Conceito: D, suas notas foram {nota1, nota2} a média ficou {media}, REPROVADO :(')

elif media >=6.0 and media <7.5:
    print (f'Conceito: C, suas notas foram {nota1,nota2} a média ficou {media}, APROVADO :D')

elif media >=7.5 and media <9.0:
    print (f'Conceito: B, suas notas foram {nota1,nota2} a média ficou {media}, APROVADO :D')

elif media >=9.0 and media <=10:
    print (f'Conceito: A, suas notas foram {nota1,nota2} a média ficou {media}, APROVADO :D')
