#  Variáveis?

name = 'Pablo'
age = 29
height = 1.75
weight = 89
older = age > 18

print('Name: ',name)
print('Age: ',age)
print('Height:', height)
print('older: ', older)

imc = weight/(height ** 2)
print(name, 'idade: ', age,  'seu imc é ',imc)
print(f'{name} tem {age} anos de idade imc:{imc:.2f}' )
print('{} {} anos,  imc {:.2f}  '.format(name, age, imc))