print('{:=^68}'.format(' \033[1;34mDROGARIA PAGUE MAIS \033[m'))
produto = float(input('Qual o valor do produto?:R$'))
print(20 * '{} = {}'.format('\033[0;34m', '\033[m'))
print('''escolha a forma de pagamento: 
Á vista Dinheiro/cheque com \033[0;32m10% de desconto\033[m [\033[;33m1\033[m] 
Á vista no Cartão com \033[0;32m5% de desconto\033[m [\033[;33m2\033[m]
Em ate 2x no cartão [\033[;33m3\033[m] 
3x ou mais no cartão com \033[0;31m20% de juros\033[m [\033[;33m4\033[m]''')
print(20 * '{} = {}'.format('\033[0;34m', '\033[m'))
ec = int(input('Digite o numero da respectiva forma de pagamento:'))
d = produto - (10 * produto / 100)
c = produto - (5 * produto / 100)
ccc = produto + (20 * produto / 100)
x = 3
if ec == 1:
    print('Você vai pagar a vista em dinheiro/cheque e o produto que custava R${:.2f} vai sair por R${:.2f}'.format(produto, d))
elif ec == 2:
    print('Você vai pagar a vista no cartão e o produto que custava R${:.2f} vai sair por R${:.2f}'.format(produto, c))
elif ec == 3:
    print('Você vai pagar no cartão em 2x sem juros, serão duas parcelas de R${:.2f}'.format(produto / 2))
elif ec == 4:
    if x <= 2:
        print('Você vai pagar no cartão em 2x sem juros, serão duas parcelas de R${:.2f}'.format(produto / 2))
    elif x >= 3:
        x = int(input('Em quantas vezes?:'))
        print('Você vai pagar em {}x no cartão e o produto que custava R${:.2f} vai sair por R${:.2f} em {} parcelas de R${}'.format(x, produto, ccc, x, ccc / x))
else:
    print('Opção inválida, escolha uma das alternativas do quadro entre 1 - 4')
