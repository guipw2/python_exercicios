from ex107 import coin

num = float(input('Type a price: '))
print(f'The half of {num} is {coin.half(num)}')
print(f'The double of {num} is {coin.double(num)}')
print(f'Increasing 10%, we have {coin.increase(num,  10)}')
print(f'Decreasing 13%, we have {coin.decrease(num, 13)}')
