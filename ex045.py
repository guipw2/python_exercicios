from random import randint
from time import sleep
print('{:=^40}'.format('JOKENPÔ'))
itens = ('\033[1;37mPedra\033[m', '\033[1;33mPapel\033[m', '\033[1;35mTesoura\033[m')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Sua jogada:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 13)
print('Jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('=-' * 13)
sleep(0.5)
if computador == 0: # computador joga PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # computador joga PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador joga TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
