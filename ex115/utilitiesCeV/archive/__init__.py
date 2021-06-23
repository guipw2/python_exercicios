def fileExists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        print('File not found')
        return False
    else:
        print('File found successfully')
        return True


def crateFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an ERROR creating the file')
    else:
        print(f'{name} file successfully created')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('ERROR reading the file')
    else:
        for line in a:
            dado = line.split(';')
            if len(dado) == 2:
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30} {dado[1]:>3} years old')
            else:
                print('', end='')
    finally:
        a.close()


def register(flnm, name='N/A', age=0):
    try:
        a = open(flnm, 'at')
    except:
        print('ERROR occurred while opening the file')
    else:
        try:
            a.write(f'\n{name};{age}')
        except:
            print('There was an ERROR writing data')
        else:
            print(f'{name} successfully added')
    finally:
        a.close()
