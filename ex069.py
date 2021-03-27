idade = sexo = continuar = contfem = contmasc = conti = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade:'))
    if idade > 18:
        conti += 1
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    while sexo not in 'MmFf':
            sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo in 'Ff' and idade < 20:
        contfem += 1
    if sexo in 'Mm':
        contmasc += 1
    continuar = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'''Total de pessoas com mais de 18 anos:{conti}
Ao todo temos {contmasc} homens cadastrados
E temos {contfem} mulheres cadastradas com menos de 20 anos''')
