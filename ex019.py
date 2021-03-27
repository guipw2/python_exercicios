from _random import choice
p = str(input('Primeiro aluno:'))
s = str(input('Segundo aluno:'))
t = str(input('Terceiro aluno:'))
q = str(input('Quarto aluno:'))
lista = [p, s, t, q]
e = choice(lista)
print('O aluno escolhido foi {}'.format(e))
