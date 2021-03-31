goals = list()
player = dict()
team = list()
while True:
    tot = 0
    player['name'] = str(input("Player's name: "))
    partidas = int(input(f'How many matches {player["name"]} played?: '))
    for c in range(1, partidas + 1):
        if c == 1:
            pos = 'st'
        elif c == 2:
            pos = 'nd'
        elif c == 3:
            pos = 'rd'
        else:
            pos = 'th'
        goals.append(int(input(f'    How many goals in the {c}{pos} match?: ')))
    player["total"] = sum(goals)
    player["goal"] = goals[:]
    goals.clear()
    team.append(player.copy())
    player.clear()
    continu3 = str(input('Want to continue? [Y/N]: ')).strip().upper()[0]
    while continu3 not in 'NnYy':
        print('ERROR! Answer only Y or N')
        continu3 = str(input('Want to continue? [Y/N]: ')).strip().upper()[0]
    if continu3 in 'Nn':
        break
print('-=' * 30)
print(f'{"code":<} {"name":<1} {"goals":^30} {"total":>10}')
print('__' * 26)
for k, v in enumerate(team):
    print(f'{k:>4} {str(v["name"]):<17}{str(v["goal"]):<24}{str(v["total"]):<5}')
print('__' * 26)
while True:
    show = int(input('Show data for which player? (999 to stop): '))
    if show == 999:
        break
    elif show > len(team):
        print(f'ERROR! There is no player with code {show}')
    else:
        print(f" -- {team[show]['name']}'s GOAL LIST:")
        for i, g in enumerate(team[show]['goal']):
            if i == 1:
                pos = 'st'
            elif i == 2:
                pos = 'nd'
            elif i == 3:
                pos = 'rd'
            else:
                pos = 'th'
            print(f'    In the {i+1}{pos} game he scored {g} goals')
    print('__' * 26)
print('<< CHECK BACK OFTEN >>')
