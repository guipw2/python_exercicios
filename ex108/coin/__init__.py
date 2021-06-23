def coin(price=0, currency='R$'):
    return f"{currency}{price:.2f}".replace('.', ',')


def half(price=0):
    price /= 2
    return coin(price)


def double(price=0):
    price *= 2
    return coin(price)


def increase(price=0, percent=0):
    i = price + (price * percent / 100)
    return coin(i)


def decrease(price=0, percent=0):
    d = price - (price * percent / 100)
    return coin(d)
