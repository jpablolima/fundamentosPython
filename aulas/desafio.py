nome  = 'Pablo'
idade = 30
altura = 1.75
peso = 89
ano_atual = 2021

ano_nascimento = ano_atual - idade

imc = peso /(altura ** 2)

print(f'{nome} tem {idade}, {altura} de altura e pesa {peso}Kg')
print(f'O imc do Pablo é de : {imc:.2f}')
print(f'Pablo nasceu: {ano_nascimento}')