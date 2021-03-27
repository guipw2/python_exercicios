from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = dict()
for k, v in jogo.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado')
print('-=' * 30)
sleep(1)
print('    == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1:>6}º lugar: {v[1]} com {v[0]}')
    sleep(0.5)
