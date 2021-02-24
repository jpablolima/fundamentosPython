# nome = 'Pablo'

# if 'h' in nome:
#     print(f'tem no {nome}')
# else:
#     print(f'não tem no {nome}')




user = input('Use: ')
password = int(input('password: '))

user_db = 'Pablo'
password_db = 123456



if(user == user_db and password == password_db):
    print('Logado')
else:
    print(f'usuário ou senha incorreto')   