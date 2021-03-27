soma = 0
cont = 0
conta = 0
for c in range(1, 7):
    num = int(input('Digite um valor:'))
    conta += 1
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você me informou {} números dos quais {} era(m) par(es) e a soma dele(s) foi {}'.format(conta, cont, soma))
