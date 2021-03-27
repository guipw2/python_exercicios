from random import randint
from time import sleep
computador = randint(1, 5)
print(15 * '-=-')
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print(15 * '-=-')
jogador = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! Você ganhou!')
else:
    print('GANHEI! Eu pensei no numero {} e nâo no {}!'.format(computador, jogador))
