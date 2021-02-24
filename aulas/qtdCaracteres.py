''' 
    len - funciona com str
'''
# usuario = input('Digite uma senha: ')

# qtd = len(usuario)
# if (qtd < 6):
#     print('A senha deve ter no mínimo de 6 digitos! Digite novamente')
# else:
#     print('A senha tem 6 digitos')

'''
    Usuário digitar um número interiro  e informar se o número é par
    caso não digite um número interiro informe que não é um número inteiro
'''

# numero = input('Digite um número inteiro: ')

# if (numero.isdigit()):
#     numero = int(numero)
#     if (numero % 2 == 0):
#         print(f'{numero} é par')
#     else:
#         print(f'{numero} ímpar')        
# else:
#     print(f'não é {numero} inteiro')

# horario =  input("Digite um horário entre 0-23: ")

# if (horario.isdigit()):
#     horario = int(horario)
#     if (horario < 0 or horario > 23):
#         print('Horário deve estar entre 0 e 23 horas.')
#     else:
#         if(horario <= 11):
#             print(f'{horario} Bom dia')
#         elif (horario <= 17):
#             print(f'{horario} Boa tarde')
#         else:
#             print(f'{horario} Boa noite')
# else:
#     print('Digite um horário entre 0 e 23.')


nome = input('Figite seu nome:')
tamanho = len(nome)

if(tamanho <= 4):
    print('nome pequeno')
elif (tamanho <= 6):
    print('tamanho do nome normal')    
else:
    print('tamanho do nome grande')

