color = {'white': '\033[;30m', 'red': '\033[;31m', 'green': '\033[;32m',
         'yellow': '\033[;33m', 'blue': '\033[;34m', 'purple': '\033[;35m',
         'cian': '\033[;36m', 'grey': '\033[;37m', 'end': '\033[m'}


def line(size=40):
    print('-' * size)


def title(msg='title not found', sz=40):
    line(sz)
    print(msg.upper().center(sz))
    line(sz)


def menu(titlename='title not found', sizeoflines=40, filename='', *msg):
    from ex115.utilitiesCeV import archive

    def resp(n):
        cont = 0
        from ex115.utilitiesCeV.archive import readFile
        from time import sleep

        while True:
            num = str(input(n))
            if num.isalpha():
                print('\033[0;31mERROR: please enter a valid integer number\033[m')
                sleep(1)
            elif num.isnumeric():
                value = int(num)
                if value == len(msg):
                    sleep(0.3)
                    title('Leaving the system... See you later')
                    sleep(1)
                    break
                elif value == 1:
                    title('registered people')
                    readFile('algoae.txt')
                    sleep(2)
                elif value == 2:
                    name = str(input('Name: '))
                    age = int(input('Age: '))
                    archive.register(file, name, age)
                    sleep(2)
                elif value > len(msg):
                    print('\033[0;31mERROR! Enter a valid option\033[m')
                    sleep(1)
            title(titlename)
            for l in range(0, len(msg)):
                print(f'{color["yellow"]}{l + 1}{color["end"]} - {color["blue"]}{msg[l]}{color["end"]}')
            line(sizeoflines)
    while True:
        file = filename
        if not archive.fileExists(file):
            archive.crateFile(file)
        title(titlename, sizeoflines)
        for l in range(0, len(msg)):
            print(f'{color["yellow"]}{l + 1}{color["end"]} - {color["blue"]}{msg[l]}{color["end"]}')
        line(sizeoflines)
        return resp(f'{color["green"]}Your option:{color["end"]} ')
