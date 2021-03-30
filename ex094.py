info = dict()
all = list()
average = 0
while True:
    info['name'] = str(input('Name: '))
    info['gender'] = str(input('Gender: ')).strip().upper()[0]
    while info['gender'] not in 'MmFf':
        print('ERROR! Please, type just M or F ')
        info['gender'] = str(input('Gender: ')).strip().upper()[0]
    info['age'] = int(input('Age: '))
    average += info['age']
    contunu3 = str(input('Want to continue? [Y/N]: ')).strip().upper()[0]
    all.append(info.copy())
    info.clear()
    while contunu3 not in 'YyNn':
        print('ERROR! Answer only Y or N')
        contunu3 = str(input('Want to continue? [Y/N]: ')).strip().upper()[0]
    if contunu3 in 'Nn':
        break
print('-=' * 25)
print(f'A) Altogether we have {len(all)} people registered')
print(f'B) Average age is {average / len(all):.2f} years')
print('C) Registered women were:', end='')
for c, v in enumerate(all):
    if v['gender'] in 'Ff':
        print(f' {v["name"]}', end='')
print(f'\nD) List of people who are above the average:')
for c, v in enumerate(all):
    if v['age'] > average / len(all):
        print(f'    name = {v["name"]}; gender = {v["gender"]}; age = {v["age"]}')
print('<< FINISHED >>')
