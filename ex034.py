slrio = float(input('Quanto você ganha?:R$'))
if slrio >= 1251:
    print('O seu aumento será de 10% e você ganhará R${:.2f}'.format(10 * slrio / 100 + slrio))
else:
    print('O seu aumento será de 15% e você ganhará R${:.2f}'.format(15 * slrio / 100 + slrio))
