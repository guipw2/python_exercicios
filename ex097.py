def write(txt):
    d = len(txt) + 4
    print('~' * d)
    print(f'  {txt}')
    print('~' * d)


write('Guilherme')
write('nothing')
