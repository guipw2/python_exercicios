def token(name='<unknown>', goals=0):
    print(f'Player {name} scored {goals} goal(s) in the league')


nm = str(input("Player's name: "))
gl = str(input('Number of goals: '))
if gl.isnumeric():
    gl = int(gl)
else:
    gl = 0
if nm.strip() == '':
    token(goals=gl)
else:
    token(nm, gl)
