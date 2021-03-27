altura = float(input('Digite sua altura:(m)'))
peso = float(input('Digite seu peso:(Kg)'))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}, o que significa que '.format(imc), end='')
if imc < 18.5:
    print('você está abaixo do peso!')
elif 18.5 < imc < 25.5:
    print('você está no peso ideal!')
elif 25.5 < imc < 30:
    print('você está com sobrepeso!')
elif 30 < imc < 40:
    print('você está obeso')
else:
    print('você está com obesidade mórbida!')
