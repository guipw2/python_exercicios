par = c3 = maior = 0
matriz = [[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0],]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if l == 1:
            maior = matriz[l][c]
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
for l in range(0, 3):
    c3 += matriz[l][2]
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {c3}')
print(f'O maior valor da segunda linha é {maior}')
