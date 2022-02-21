
#Trabalhando com Arquivos

#arquivo = open('palavras.txt', 'w')

#Abrir imagem
'''
imagem = open('foto.jpg', 'rb')
'''
'''
arquivo.write('banana\n')
arquivo.write('melancia\n')
arquivo.write('morango\n')
arquivo.write('manga\n')

arquivo.close()
'''
arquivo = open('palavras.txt', 'r')
palavras=[]

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

    print(linha)
arquivo.close
