def jogar():
    
    import random
    
    print('***********************************')
    print('*          Jogo da Forca          *')
    print('***********************************')

    arquivo = open('palavras.txt', 'w')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input('Qual a Letra? ')

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    #print('Encontrei a letra {} na posição {}'.format(letra, posicao))
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print('você ganhou')
    else:
        print('Você Perdeu')

        # break

    print('Fim de Jogo')
