lista = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no fim da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na {pos}ª posição')
                break
            pos += 1
print('Os valores digitados na lista foram {}')
