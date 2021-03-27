casa = float(input('Valor da casa:R$'))
salario = float(input('Seu salário:R$'))
ano = int(input('Em quantos anos você pretende pagar?'))
tempo = casa / (ano * 12)
prct = 30 * salario / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print(' a prestação sairá por R${:.2f}'.format(tempo))
if tempo >= prct:
    print('Empréstimo negado')
    #print('Calculando com base no seu salario e o tempo que você pretende pagar voce não conseguirá pagar o empretimo')
else:
    print('Empréstimo aprovado')
