# -*- coding: utf-8 -*-
#w = open("arquivos2.txt", "w") #Criar arquivo2 o modo w deleta o conteudo e grava um novo

w = open("arquivos2.txt", "a") # O modo a ele incrementa conteudos

#escrever no arquivo
w.write("Esse é o meu arquivo\n")

w.close() # É importante fechar o arquivo logo depois