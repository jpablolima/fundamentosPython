'''
Operadores
+ ,  - , *, / , //, %, ** 

'''

# print('Soma: ', 10+2 )
# print('Subtração: ', 10 - 2 )
# print('Multiplicação: ', 10 * 2 )
# print('Divisão: ', 10/3 )
# print('Divisão inteiro: ', 10 // 2 )
# print('Resto da Divisão: ', 10 % 3 )
# print('Potênciação: ', 10 ** 2 )



# Observe o trecho de código abaixo.
# int ÍNDICE = 13, SOMA = 0, K = 0; 
# enquanto K <INDICE faça {K = K + 1; 
# SOMA = SOMA + K; } imprimir (SOMA); 
# Ao final do processamento, qual será o valor da variável SOMA?

# indice = 13
# soma = 0 
# k = 0

# while k < indice:
#     k = k + 1
#     soma = soma + k
# print(soma)


fibonacci = [0,1]
i = 0
numero = int(input("Digite um número: "))

while numero > len(fibonacci):
	fibonacci.append(fibonacci[i] + fibonacci[i+1])
	i+=1

print ('Fibonacci:', numero,'=',(fibonacci[numero-1]))