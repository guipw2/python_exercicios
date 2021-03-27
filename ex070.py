total = maisd1000 = cont = menor = 0
menorp = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço:R$'))
    cont += 1
    if preco > 1000:
        maisd1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        menorp = produto
    total += preco
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'''O total da compra foi R${total:.2f}
Temos {maisd1000} produto qu custa mais de R$1000.00
O produto mais barato foi {menorp} que custa R${menor:.2f}''')
