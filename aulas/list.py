# Lista

''' 
    Listas em Python 
    fatiamento 
    append, insert, pop, del, clear, extend, min, max
    range
'''


heroes = ['Iron man', 'WANDA MAXIMOFF', 'BLACK WIDOW', 'Supergirl', 'Mulher Maravilha']
marvel = ['Iron man', 'WANDA MAXIMOFF','BLACK WIDOW']
dc = ['Batman', 'Supergirl', 'Mulher Maravilha']
dragon_ball = ['Goku', 'Vegeta', 'Jiren', 'Freeza', 'Gohan', 'Majin Boo','Goten', 'Trunks', 'Piccolo', 'Pan']


marvel.extend(dc)

dc.extend('Goku')
marvel.append('Vegeta')


gerandoList = list(range(1,10))
l1 = gerandoList;
# l = list(range(1,10,2))
# print(gerandoList)
# print(l)
# print(l1)

# soma = 0
# for valor in l1:
#     print(valor)
#     soma = soma + valor
# print(f'Soma dos valores da Lista: {soma} ')


# numbers = [10,2,3,4,1.5]
# numbers.insert(0, 72)
# numbers.pop();
# del(numbers[1:3])
# print(numbers)
# print(max(numbers))
# print(min(numbers))

# comics = marvel + dc;

# print(heroes)
# print(heroes[0:2])
# print(heroes[::2])
# print(heroes[-1])
# print(numbers)
# print(comics)
# print('Marvel' ,marvel)
# print('DC ', dc)
# print('Dragon Ball', dragon_ball)
# print(numbers)


# Palavra Secreta

secreto = 'python'
digitados = []
chances = 3


while True:

    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Não vale, digite apenas uma letra.")
        continue
    
    digitados.append(letra)

    if letra in secreto:
        print(f' A letra "{letra}" existe na palavra secreta')
        continue
    else:
        print(f'A letra não "{letra}" não existe na palavra secreta')
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print(f'Você Ganhou!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
    print()
