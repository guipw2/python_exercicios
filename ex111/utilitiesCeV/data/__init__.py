def readInt(n):
    value = 0
    ok = False
    while True:
        num = str(input(n))
        if num.isnumeric():

            value = int(num)
            ok = True
        else:
            print('\033[0;31mERROR! enter a valid integer number\033[m')
        if ok:
            break
    return value


def readMoney(msg):
    ok = False
    while not ok:
        entry = str(input(msg)).replace(',', '.').strip()
        if entry.isalpha() or entry == '':
            print(f'\033[0;31mERROR: "{entry}" is an invalid price\033[m')
        else:
            ok = True
            return float(entry)
