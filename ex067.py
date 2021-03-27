n = cont = 0
tabuada = 'TABUADA'
print('-' * 40)
print(f'{tabuada:^40}')
print('-' * 40)
while True:
    n = int(input('Quer ver a tabuada de qual número?:'))
    print('-' * 35)
    if n <= 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
    print('-' * 35)
    cont = 0
print('Programa TABUADA \033[31mENCERRADO\033[m. Volte nunca!')
