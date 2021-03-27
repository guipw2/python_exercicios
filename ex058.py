from random import randint
from time import sleep
computador = randint(1, 10)
print('Sou seu computador...')
sleep(0.9)
print('Vou pensar em um numero entre 0 e 10.')
sleep(1.5)
print('Será que voce consegue adivinhar qual foi?')
sleep(1.5)
acertou = False
conttent = 0
while not acertou:
    jogador = int(input('Qual seu palpite:'))
    conttent += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais... Tente novamente.')
    elif jogador > computador:
        print('Menos... Tente novamente.')
if conttent == 1:
    print('Nossa! Você acertou de primeira. Que sorte!')
elif 2 <= conttent <= 4:
    print(f'Você acertou em {conttent} tentativas. Parabens!')
elif 5 <= conttent <= 7:
    print(f'Você acertou em {conttent} tentativas.')
else:
    print('Z',end='')
    sleep(1)
    print('z',end='')
    sleep(1)
    print(f'ZzZz... Ah! Você acertou em {conttent} tentativas. Demorou hein!?')
