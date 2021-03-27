nota1 = float(input('Digite a 1ª nota:'))
nota2 = float(input('Digite a 2ª nota:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO! Estude mais, nos vemos denovo ano que vem.')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO! Etude, você ainda tem mais uma chance.')
elif media >= 7.0:
    print('APROVADO! Parabéns, continue assim!')
