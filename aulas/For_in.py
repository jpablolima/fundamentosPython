# nome = 'Pablo'

# for letra in nome:
#     print(letra)

# for n, letra in enumerate(nome):
#     print(n, letra)

# for numero in range(10):
#     print(numero)

# for numero in range(1,10,2):
#     print(numero)

# print('##### Número Par ####')
# for n in range(100):
#     if (n % 2 == 0):
#         print(n)

texto = 'javaScript'
nova_string = ''


for letra in texto:
    if letra == 'a':
        nova_string = nova_string + letra.upper()
    elif letra == 'i':
        nova_string = nova_string + letra.upper()
    elif letra == 'S':
        nova_string = nova_string + letra.lower()
    else:
        nova_string += letra
print(nova_string)
