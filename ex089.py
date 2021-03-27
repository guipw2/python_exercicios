# Boletim com listas compostas:
from time import sleep
lista = list()
geral = list()
while True:
    nome = str(input('Nome:'))
    not1 = float(input('1º Nota:'))
    not2 = float(input('2º Nota:'))
    med = (not1 + not2) / 2
    lista.append([nome, [not1, not2], med])
    geral.append(lista[:])
    lista.clear()
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()
    if continuar in 'Nn':
        break
print('-=' * 25)
print('No. NOME        MÉDIA')
print('-' * 25)
for n, l in enumerate(geral):
    print(f'{n:<1} {l[0]:^6}{l[2]:>13.1f}')
while True:
    print('-' * 30)
    nota = int(input('Mostrar as notas de qual aluno? (999 interrompe)'))
    if nota >= 999:
        break
    print(f'As notas de {geral[nota][0]} são {geral[nota][1]}')
sleep(0.5)
print('FINALIZANDO...')
sleep(0.5)
print(f'<<< VOLTE SEMPRE >>>')
