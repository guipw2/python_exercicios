matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('-=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''matriz = [[], [], []]
while True:
    for v in range(0, 3):
        m1 = int(input(f'Digite um numero para [0, {v}]:'))
        matriz[0].append(m1)
    for v in range(0, 3):
        m2 = int(input(f'Digite um numero para [1, {v}]:'))
        matriz[1].append(m2)
    for v in range(0, 3):
        m3 = int(input(f'Digite um numero para [2, {v}]:'))
        matriz[2].append(m3)
    break
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')'''
