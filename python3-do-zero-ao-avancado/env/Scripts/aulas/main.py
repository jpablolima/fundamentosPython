# number = 10;

# chute =  int(input("Digite um número: "))

# if(chute == number):
#    print('Paranbéns, você acertou!')
# elif(chute > number):
#    print('O número digitado foi maior! Tente novamente')
# elif(chute < number):
#    print('O número digitado foi menor! Tente novamente')

# numero_certo = 10;
# chute = int(input("Digite um valor: "))
# acertou = chute == numero_certo;
# maior = chute > numero_certo;
# menor = chute < numero_certo;


# if(acertou):
#    print('Parabéns, você acertou', numero_certo)
# elif(maior):
#    print('Erroo, o valor digitado é maior')
# elif(menor):
#    print('Errooo, o valor digitado é menor') 



# x = 10;
# while (x >  0):
#    print(x)
#    x = x  - 1

# numero_certo =  10;
# tentativas = 3;

# while(tentativas > 0):
#    chute = int(input('Digite um número: '))
#    print("você digitou: ", chute)

#    acertou = chute == numero_certo;
#    maior = chute > numero_certo;
#    menor = chute <  numero_certo;

#    if(acertou):
#       print('Parabéns você acertou', chute)
#       break
#    elif(maior):
#       print('Erroo, o número digitado é maior')
#    elif(menor):
#       print('Erroo, o número digitado é menor')
   
#    tentativas =  tentativas - 1

# numero_secreto = 10;
# tentativas=5;

# for rodada in range(1, tentativas):
#    print('tentativas: ', rodada,' de ' , tentativas)

#    chute = int(input('Digite um número: '))
#    print(chute)

#    acertou = numero_secreto == chute
#    maior = numero_secreto > chute
#    menor = numero_secreto < chute

#    if(acertou):
#       print('Você acertou')
#       break
#    elif(maior):
#       print('errooo, número digitado')
#    elif(menor):
#       print('erroo, o número digitado é menor')



# a = 1;
# b = 0
# while (b > 3):
#     a = a +1
#     b = b +1

# print(a)

# s = 0;
# for x in range(1,100):
#     s = s + x
# print(s)


# s = 0
# x = 1
# while (x < 100):
#     s = s + x
#     x = x + 1
# print(s)


# times = ['flamengo','barça', 'milan']

# for time in times:
#     print(time)
# times.append('inter')
# print(times)

# for i, time in enumerate(times):
#     print (i + 1, '=>', time)


# x = 10;
# y = 5;
# soma = ((x + y)/2) 
# print(soma)

# Calculo de volume de uma esfera
import math

r = float(input('Digite o valor do raio? '))
volume = (4 / 3 * math.pi * (r ** 3));
print(volume)


# print(math.sqrt(25))