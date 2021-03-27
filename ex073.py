times = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athlético Paranaense', 'RB Bragantino',
         'Ceará', 'Corinthians', 'Atlético Goianiense', 'Bahia', 'Sport Recife',
         'Fortaleza EC', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('-='* 15)
print(f'Listas de times Brasileirão: {times}')
print('-='* 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='* 15)
print(f'Os ultimos 4 são: {times[-4:]}')
print('-='* 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='* 15)
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posição')
