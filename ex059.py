n1 = float(input('Primeiro valor:'))
n2 = float(input('Segundo valor:'))
opçao = 0
maior = 0
menor = 0
while opçao != 7:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] menor
    [ 5 ] novos números
    [ 6 ] elevar o numero
    [ 7 ] sair do programa''')
    opçao = int(input('>>>>> Qual é a sua opção?'))
    if opçao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
        print(10 * '=-=')
    elif opçao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
        print(10 * '=-=')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
        print(10 * '=-=')
    elif opçao == 4:
        if n1 < n2:
            menor = n1
        elif n2 < n1:
            menor = n2
        print(f'Entre {n1} e {n2} o menor é {menor}')
        print(10 * '=-=')
    elif opçao == 5:
        print('Informe os número novamente:')
        n1 = float(input('Primeiro valor:'))
        n2 = float(input('Segundo valor:'))
        print(10 * '=-=')
    elif opçao == 6:
        print(f'{n1} elevado a {n2} é igual a {pow(n1, n2)}')
    elif opçao == 7:
        print('Finalizando...')
        sleep(1.5)
        print(10 * '=-=')
    else:
        print('Opção inválida. Tente novamente!')
        print(10 * '=-=')
print('Fim do programa! Volte sempre!')
