dado = []
galera = []
mai = men = 0
while True:
    dado.append(str(input('Nome:')))
    dado.append(float(input('Peso:')))
    if len(galera) == 0:
        men = mai = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men}. Peso de ', end='')
for op in galera:
    if op[1] == men:
        print(f'{op[0]}')
