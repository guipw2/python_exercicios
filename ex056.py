soma = 0
media = 0
maiorhm = 0
nomevelho = ''
contm = 0
for p in range(1, 5):
    print(f'-----{p}ªPESSOA-----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    m = 'M'
    f = 'F'
    soma += idade
    if sexo in 'Ff' and idade < 20:
        contm += 1
    if p == 1 and sexo in 'Mm':
        maiorhm = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhm:
        maiorhm = idade
        nomevelho = nome
    if contm == 1:
        moça = 'mulher'
    else:
        moça = 'mulheres'
media = soma / 4
print('A media de idade é {} anos'.format(media))
print(f'O homem mais velho tem {maiorhm} anos e se chama {nomevelho}')
print(f'Tem {contm} {moça} com menos de 20 anos')
