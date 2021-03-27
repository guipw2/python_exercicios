lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        print('Valor\033[1;32m adicionado\033[m com\033[1;32m sucesso!\033[m...')
        lista.append(n)
    else:
        print('Valor duplicado! \033[4;31mNão\033[m vou \033[4;31madicionar\033[m...')
    continuar = str(input('Continuar [S/N]:')).strip().upper()[0]
    if continuar in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
