velo = float(input('Digite a velocidade do carro:'))
if velo > 81:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((velo - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')
