print('***********************************')
print('*      Jogo da Adivinhação        *')
print('***********************************')

numero = 42
tentativas = 3
rodada = 1

while (tentativas > 0):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número: '))
    print('Você digitou: {}' .format(chute))

    acertou = numero == chute
    maior = chute > numero
    menor = chute < numero
    
    if (acertou):
        print('Você acertou!!')
        break
    elif(maior):
        print('Você Errou! o seu numero é maior')
    elif(menor):
        print('Você Errou! o seu numero é menor')
    
    rodada = rodada + 1
    
    if (rodada==(tentativas+1)):
        break
        
print('Fim de Jogo')
