from datetime import date
maquina = date.today().year
conti = 0
contj = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(c)))
    idade = maquina - ano
    if idade > 18:
        conti += 1
    elif idade < 18:
        contj += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(conti))
print('E também tivemos {} pessoas menores de idade'.format(contj))
