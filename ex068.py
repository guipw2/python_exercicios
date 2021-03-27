from random import randint
nj = computador = t = v = 0
jj = ''
while True:
    computador = randint(1, 20)
    nj = int(input('Digite um valor: '))
    jj = str(input('Par ou Ímpar? ')).upper().strip()[0]
    while jj not in 'PI':
        jj = str(input('Par ou Ímpar?')).upper().strip()[0]
    t = computador + nj
    print(f'Você jogou {nj} e o computador {computador}. Total de {t} ',end='')
    print('DEU PAR!' if t % 2 == 0 else 'DEU ÍMPAR!')
    if jj == 'P':
        if t % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if jj == 'I':
        if t % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {v} vezes.')
