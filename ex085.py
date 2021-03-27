lista = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor:'))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-=' * 25)
lista.sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
