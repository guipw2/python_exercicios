def readInt(n):
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERROR: please enter a valid integer number\033[m')
            continue
        except KeyboardInterrupt:
            print('Data entry interrupted by the user')
            return 0
        else:
            return num


def readFloat(n):
    while True:
        try:
            num = float(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERROR: please enter a valid real number\033[m')
            continue
        except KeyboardInterrupt:
            print('Data entry interrupted by the user')
            return 0
        else:
            return num


intgr = readInt('Type an Integer number: ')
real = readFloat('Type an Real number: ')
print(f'The entire value entered was {intgr} and the real value was {real}')
