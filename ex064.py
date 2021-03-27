t = n = 0
cont = 0
n = int(input('Digite um numero [999 pra parar]:'))
while n != 999:
    t += n
    cont += 1
    n = int(input('Digite um numero [999 pra parar]:'))
print(f'Você digitou {cont} números e a soma entre eles é {t}')