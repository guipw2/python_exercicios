sexo = str(input('Informe seu sexo: [M/F]')).lower().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido. Por favor digite seu sexo novamente:')).lower().strip()[0]
if sexo == 'm':
    sexo = 'masculino'
else:
    sexo = 'feminino'
print(f'Sexo {sexo} registrado com sucesso!')

