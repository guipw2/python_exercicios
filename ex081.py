list = []
while True:
    n = int(input('Digite um valor:'))
    list.append(n)
    c = str(input('Você quer continuar? [S/N]:')).strip().upper()[0]
    if c in 'Nn':
        break
print(f'Você digitou {len(list)} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente são {list}')
print(f'O valor 5 ', end='')
if 5 not in list:
    print('não foi encontrado na lista!')
else:
    print('faz parte da lista!')
