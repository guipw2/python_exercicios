from random import randint
jogos = []
lista = []
n = randint(1, 60)
user = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 0
while tot < user:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    tot += 1
    lista.clear()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

#print(f'''{'-' * 40}
#{'JOGO DA MEGA SENA':^40}
#{'-' * 40}''')
'''n = int(input('Quantos jogos você quer que eu sorteie?: '))
if n == 1:
    jogo = 'JOGO'
else:
    jogo = 'JOGOS'
print(f'{"-=" * 3} SORTEANDO {n} {jogo} {"=-" * 3}')
sleep(0.5)
for jgs in range(0, n):
    print(f'Jogo {jgs + 1}: [-> ', end='')
    for j in range(0, 6):
        print(f'{randint(1, 60)} ', end='')
    print('<-]')
    sleep(1)
print(f'{"-=" * 5} < BOA SORTE! > {"=-" * 5}')'''
