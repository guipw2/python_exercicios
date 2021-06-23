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


nmbr = readInt("Type a number: ")
print(f'You just entered the number {nmbr}')

