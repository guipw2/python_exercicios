n1 = input('Digite algo:')
print('Qual o tipo primitivo?', type(n1))
print('Só tem espaços?', n1.isspace())
print('É alfa-numerico?', n1.isalnum())
print('É um numero?', n1.isnumeric())
print('É uma letra?', n1.isalpha())
print('Está maiusculo?', n1.isupper())
print('Esta minusculo?', n1.islower())
print('Está capitalizada?', n1.istitle())