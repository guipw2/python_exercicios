extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
resp = int(input('Digite um numero entre 0 e 20:'))
while True:
    if 0 <= resp <= 20:
        break
    resp = int(input('Tente novamente. Digite um numero entre 0 e 20:'))
print(f'Você digitou o numero {extenso[resp]}')
continuar = str(input('Você quer continuar?:[S/N]')).strip().upper()[0]
while True:
    if continuar in 'Nn':
        break
    if continuar in 'Ss':
        resp = int(input('Digite um numero entre 0 e 20:'))
        print(f'Você digitou o numero {extenso[resp]}')
        continuar = str(input('Você quer continuar?')).strip().upper()[0]
    else:
        continuar = str(input('Tente novamente. Você quer continuar?')).strip().upper()[0]
print('Fim!')
