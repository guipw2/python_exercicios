goals = list()
player = dict()
team = list()
while True:
    tot = 0
    player['name'] = str(input("Player's name: "))
    partidas = int(input(f'how many matches {player["name"]} played?: '))
    for c in range(1, partidas + 1):
        if c == 1:
            pos = 'st'
        elif c == 2:
            pos = 'nd'
        elif c == 3:
            pos = 'rd'
        else:
            pos = 'th'
        goal = int(input(f'    how many goals in the {c}{pos} match?: '))
        goals.append(goal)
        tot += goal
    player["total"] = tot
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
print(f'{"cod":<} {"name":<1} {"goals":^30} {"total":>5}')
print('_' * 45)
for c, v in enumerate(team):
    print(f'{c:<}{v["name"]:<1}{v["goal"]:^30}{v["total"]:>5}')
