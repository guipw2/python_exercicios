continuar = 'S'
s = menor = maior = c = n = cont = media = 0
while continuar in 'Ss':
    n = int(input('Digite um numero:'))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N]:')).lower().strip()[0]
    media = s / cont
print(f'Você digitou {cont} números e a media foi {media}\nO maior valor foi {maior} e o menor {menor}')
