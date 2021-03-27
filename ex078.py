mai = men = 0
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um numero para a posiçao {cont}:')))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]
print('-=' * 20)
print(f'Você digitou os valores {valores}', end='')
print(f'O maior valor digitado foi {max(valores)} e estava na posiçao ', end='')# {valores.index(max(valores))}
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} e estava na posição ', end='')# {valores.index(min(valores))}
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}... ', end='')
