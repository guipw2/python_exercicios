from datetime import date
from time import sleep
dici = dict()
dici['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dici['idade'] = date.today().year - ano
dici['cart'] = int(input('Casrteira de Trabalho (0 não tem): '))
if dici['cart'] != 0:
    dici['anocont'] = int(input('Ano de contratação:'))
    dici['salário'] = float(input('Salário: R$'))
    dici['apos'] = 35 - (date.today().year - dici['anocont']) + dici['idade']
print('-=' * 25)
for k, v in dici.items():
    print(f' - {k} tem o valor {v}')
    sleep(0.5)
