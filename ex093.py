gol = list()
tot = 0
dici = dict()
dici['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dici["nome"]} jogou?: '))
for c in range(0, partidas):
    gols = int(input(f'    Quantos gols na {c + 1}ª partida?: '))
    gol.append(gols)
    tot += gols
dici['gols'] = gol[:]
dici['total'] = tot
print('-=' * 25)
print(dici)
print('-=' * 25)
for k, v in dici.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {dici["nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'   => Na {c + 1}ª partida, fez {dici["gols"][c]} gols.')
print(f'Foi um total de {dici["total"]} gols')
