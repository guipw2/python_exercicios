dici = dict()
dici['nome'] = str(input('Nome: '))
dici['média'] = float(input(f'Média de {dici["nome"]}: '))
print('-=' * 25)
if dici['média'] < 5.0:
    dici['situação'] = 'Reprovado'
elif 5 < dici['média'] < 7:
    dici['situação'] = 'Recuperação'
else:
    dici['situação'] = 'Aprovado'
for k, v in dici.items():
    print(f' - {k} é igual a {v}')
