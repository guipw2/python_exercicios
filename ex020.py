from random import shuffle
p = str(input('Primeiro aluno:'))
s = str(input('Segundo aluno:'))
t = str(input('Terceiro aluno:'))
q = str(input('Quarto aluno:'))
l = [p, s, t, q]
shuffle(l)
print('A ordem de apresentação será:',l)
