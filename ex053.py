print('DETECTOR DE PALÍNDROMO')
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
'''inverso = '''''
'''for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('Essa frase não é um PALÍNDROMO!')
