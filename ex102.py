def factorial(n, show=False):
    """
    -> Calculates the factorial of a number.
    :param n: number to be calculated
    :param show: show or not the account
    :return: The factorial value of a number n
    """
    print('-=' * 20)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c == 1:
                print(f' = {f}')
            else:
                print(" x ", end='')
    if not show:
        return f


print(factorial(5))
help(factorial)
