def area(w, l):
    x = w * l
    print(f'The area of a {w:.2f}x{l:.2f} plot is {x:.2f}m².')


def title():
    print('-' * 30)
    print(f'{"Terrain Control":^30}')
    print('-' * 30)


title()
width = (float(input('WIDTH (m):')))
length = (float(input('LENGTH (m):')))
area(width, length)
