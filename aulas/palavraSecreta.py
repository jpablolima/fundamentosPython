
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