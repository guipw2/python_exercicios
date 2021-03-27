from datetime import date
ano = int(input('Em que ano você nasceu?'))
maquina = date.today().year
tempo = maquina - ano
print('Quem naceu em {} agora em {} tem {} anos'.format(ano, maquina, tempo))
if tempo == 18:
    print('Já está na hora de se alistar!')
elif tempo > 18:
    saldo = tempo - 18
    print('Você se atrasou por {} ano(s), já passou da hora de se alistar!'.format(saldo))
    print('Seu alistamento foi em {}'.format(maquina - saldo))
elif tempo < 18:
    saldo = 18 - tempo
    print('Ainda faltam {} ano(s)'.format(saldo))
    print('Seu alistamento será em {}'.format(maquina + saldo))
