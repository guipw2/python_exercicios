list = []
listpar = []
listimpar = []
while True:
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        listpar.append(n)
    elif n % 2 == 1:
        listimpar.append(n)
    list.append(n)
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'A lista completa é {list}')
listpar.sort() and listimpar.sort()
print(f'A lista de pares é {listpar}')
print(f'A lista de ímpares é {listimpar}')
