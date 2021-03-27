pssg = float(input('Digite a distância da viagem:'))
if pssg >= 201:
    print(20 * '-=-')
    print('A passagem custará R${:.2f}'.format(pssg * 0.45))
    print(20 * '-=-')
else:
    print(20 * '-=-')
    print('A passagem custará R${:.2f}'.format(pssg * 0.50))
    print(20 * '-=-')
