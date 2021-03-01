''' 
 while => utilizados para realizar ações enquanto 
 uma condição for verdadeira.
'''


nome = 'Pablo'
count = 0;

while (count <  len(nome)):
    print(nome[count])
    count += 1


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


# while True:
#     print()
#     number1 = input('Digite um número: ')
#     number2 = input('Digite outro número: ')
#     operador = input('Digite o operador: ')
#     sair = input('Deseja sair? [s]im ou [n]ão ')
    
#     if (sair == 's'):
#         break

#     if not number1.isnumeric() or not number2.isnumeric():
#         print('Você precisa digitar um número')
#         continue

#     number1  = int(number1)
#     number2  = int(number2)

#     if(operador == '+'):
#         print(number1 + number2)
#     elif(operador == '-'):
#         print(number1 - number2)
#     elif(operador == '/'):
#         print(number1 / number2)
#     elif(operador == '*'):
#         print(number1 * number2)
#     else:
#         print('Operador não encontrado')


# count = 0;

# while (count < 10):
#     print(count)
#     count += 1;

# contador = 1;
# acumulador  = 1;

# while (contador <= 10):
#     print(contador, acumulador)
#     acumulador = acumulador + contador;
#     contador += 1;
    
# while (contador <= 10):
#     print(contador, acumulador)
#     if (contador > 5):
#         break

#     acumulador = acumulador + contador

#     contador += 1    
# else:
#     print('Isso será executado.')



frase = 'O rato roeu a roupa do rei de Roma'
tamanho = len(frase)
contador = 0;
nova_string = ''
# print(tamanho)

while contador < tamanho:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    contador +=1
    print(nova_string)
print(nova_string)

