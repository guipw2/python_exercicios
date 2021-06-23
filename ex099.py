from time import sleep


def bigger(*num):
    print('-=' * 25)
    print('Analyzing past values...')
    for n in num:
        print(f' {n}', end='', flush=True)
        sleep(0.5)
    if len(num) == 0:
        print(f'0. 0 values were reported in total')
        print(f'the highest value was 0')
    else:
        print(f'. {len(num)} values were reported in total')
        print(f'the highest value was {max(num)}')


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger()
