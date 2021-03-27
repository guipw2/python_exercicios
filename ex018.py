from math import radians
from cmath import sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {}° \nTem o SENO de {:.2f}. \nO COSSENO de {:.2f}. \nE a TANGENTE de {:.2f}.'.format(a, s, c,t))
