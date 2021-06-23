def coin(price=0, currency='R$'):
    return f"{currency}{price:.2f}".replace('.', ',')


def half(price=0, formatted=True):
    price /= 2
    return price if not formatted else coin(price)


def double(price=0, formatted=True):
    price *= 2
    return price if not formatted else coin(price)


def increase(price=0, percent=0, formatted=True):
    i = price + (price * percent / 100)
    return i if not formatted else coin(i)


def decrease(price=0, percent=0, formatted=True):
    d = price - (price * percent / 100)
    return d if not formatted else coin(d)


def resume(p=0, i=0, d=0):
    def t(txt='N/A'):
        print('-' * 35)
        print(f'{txt:^35}')
        print('-' * 35)
    t('SUMMARY OF VALUE')
    print(f'''Analyzed price: \t{coin(p)}
Twice the price: \t{double(p)}
Half-price: \t\t{half(p)}
{i}% Increase: \t\t{increase(p, i)}
{d}% Decrease: \t\t{decrease(p, d)}''')
    print('-' * 35)
