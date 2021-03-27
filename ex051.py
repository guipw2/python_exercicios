prim = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = prim + (10 - 1) * razao
for pa in range(prim, decimo + razao, razao):
    print('{} '.format(pa, end=' → '))
