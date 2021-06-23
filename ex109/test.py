from ex109 import coin

num = float(input('Type a price: '))
print(f'The half of {coin.coin(num)} is {coin.half(num,False)}')
print(f'The double of {coin.coin(num)} is {coin.double(num,False)}')
print(f'Increasing 10%, we have {coin.increase(num,  10)}')
print(f'Decreasing 13%, we have {coin.decrease(num, 13)}')
