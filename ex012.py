p = float(input('Valor do Produto: R$'))
d = 5 * p / 100
t = p - d
print('Com 5% de desconto você economiza R${:.2f} pagando no total R${:.2f} .'.format(d, t))
