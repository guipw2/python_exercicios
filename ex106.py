def manual():
    from time import sleep
    while True:
        print('\033[1;42m~' * (len('PyHELP HELP SYSTEM') + 4))
        print('  PyHELP HELP SYSTEM')
        print('~' * (len('PyHELP HELP SYSTEM') + 4))
        print('\033[m', end='')
        sleep(0.5)
        resp = str(input('Function or Library > ')).strip()
        if resp == 'end':
            break
        sleep(0.15)
        print('\033[1;44m~' * (len(f'Accessing the {resp} command manual') + 4))
        print(f"  Accessing the '{resp}' command manual")
        print('~' * (len(f'Accessing the {resp} command manual') + 4), '\n\033[m', end='')
        sleep(1)
        print('\033[7;40m')
        help(resp)
        print('\033[m', end='')
    sleep(0.5)
    print('\033[1;46m~' * (len('see you later!') + 4))
    print('  SEE YOU LATER!')
    print('~' * (len('see you later!') + 4))
    print('\033[m')


manual()
