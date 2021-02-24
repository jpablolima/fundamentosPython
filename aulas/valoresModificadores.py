number1 = 10
number2  = 3

divisao = number1 / number2

print(f'{divisao:.2}')
print(f'{number2:0>10}')
print(f'{number2:0<10}')
print(f'{number2:0^10}')

nome = 'Pablo'
sobrenome = 'lima'
nome_formatado = '{} {s}'.format(nome, s=sobrenome)
print(nome_formatado)
print(nome.lower())
print(nome.upper())
print(nome.title())

