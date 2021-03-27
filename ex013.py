sa = float(input('Seu salário: R$'))
a = 15 * sa / 100
sf = sa + a
print('Com aumento de 15% seu aumento é de R${:.2f}, totalizando: R$ {:.2f}'.format(a, sf))
