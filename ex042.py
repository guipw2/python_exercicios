print(15 * '\033[1;36m-=-\033[m')
print('\033[1;37mAnalizador de Triângulos')
print(15 * '\033[1;36m-=-\033[m')
r1 = float(input('\033[0;37mPrimeiro seguimento:'))
r2 = float(input('\033[0;37mSegundo seguimento:'))
r3 = float(input('\033[0;37mTerceiro seguimento\033[m'))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[;32mOs seguimentos acima PODEM FORMAR um triângulo', end='')
    if r1 == r2 == r3:
        print(' \033[4;33mEQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print(' \033[4;34mESCALENO!')
    else:
        print(' \033[4;35mISÓCELES')
else:
    print('Os seguimentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format('\033[;31m', '\033[m'))