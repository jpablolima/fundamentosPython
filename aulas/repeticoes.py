''' 
 while => utilizados para realizar ações enquanto 
 uma condição for verdadeira.
'''

#  loop infinito

# while True:
#     nome = input('nome:')
#     print(f'{nome}')

x = 0
y = 0
z = 0
# while x < 5:
#     print(x) 
#     x = x +1

# while y < 5:
#     if(y == 3):
#         y = y + 1
#         break
#     print(y)
#     y = y + 1

# while (z < 10):
#     print(z)
#     z +=1


# a = 0

# while (a < 1000000000000):
#     b = 0
#     while(b < 5):
#         print(f'{a},{b}')
#         b +=1
#     a +=1


# Calc


while True:
    print()
    number1 = input('Digite um número: ')
    number2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão ')
    
    if (sair == 's'):
        break

    if not number1.isnumeric() or not number2.isnumeric():
        print('Você precisa digitar um número')
        continue

    number1  = int(number1)
    number2  = int(number2)

    if(operador == '+'):
        print(number1 + number2)
    elif(operador == '-'):
        print(number1 - number2)
    elif(operador == '/'):
        print(number1 / number2)
    elif(operador == '*'):
        print(number1 * number2)
    else:
        print('Operador não encontrado')