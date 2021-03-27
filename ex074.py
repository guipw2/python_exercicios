from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os numeros sorteados foram:', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {(max(numeros))}')
print(f'O menor valor soteado foi {min(numeros)}')
'''cont = maior = menor = 0
for numeros in range(0, 5):
    n = (randint(1, 10))
    print(n, end='')
while cont < 5:
    n = (randint(1, 10))
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print(f'{n} ', end='')
    cont += 1'''
'''print('')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor soteado foi {menor}')'''
