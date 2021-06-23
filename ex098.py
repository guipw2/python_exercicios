from time import sleep


def counter(bg, md, end):
    if md < 0:
        md += 1
    if md == 0:
        md = 1
    print('-=' * 20)
    print(f'Count from {bg} to {end} from {md} in {md}')
    sleep(1.5)
    if bg > end:
        for nmbs in range(bg, end - md, -md):
            print(nmbs, end=' ', flush=True)
            sleep(0.5)
        print('END!')
        print('-=' * 20)
    else:
        for nmbs in range(bg, end + md, md):
            print(nmbs, end=' ', flush=True)
            sleep(0.5)
        print('END!')
        print('-=' * 20)


counter(1, 1, 10)
counter(10, 2, 0)
print("now it's your turn to customize the counts!")
bg = int(input('Beginning: '))
end = int(input('End: '))
md = int(input('Jumping: '))
counter(bg, md, end)
