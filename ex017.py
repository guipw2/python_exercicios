from math import sqrt
co = float(input('Medida do cateto oposto:'))
ca = float(input('Medida do cateto adjacente:'))
h = sqrt((ca**2)+(co**2))
print('A hipotenusa vai medir: {:.2f}'.format(h))
