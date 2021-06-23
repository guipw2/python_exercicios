from random import randint
from time import sleep


def draw(ls):
    print('Sorting 5 numbers from list:', end='')
    for count in range(0, 5):
        n = randint(1, 10)
        ls.append(n)
        print(f' {n}', end='', flush=True)
        sleep(0.25)


def sumpairs(nmbrs):
    s = count = 0
    for p in nmbrs:
        if nmbrs[count] % 2 == 0:
            s += nmbrs[count]
        count += 1
    print(f'\nAdding the even values of {nmbrs}, we have {s}')


lis = list()
draw(lis)
sumpairs(lis)
