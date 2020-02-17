#Tem como manipular arquivos de textos, documentos tabelas no python

"""
Função open
variavel = open(nome, modo) nome  = nome do arquivo
existe 6 tipos de modo

| modo | Função
|   r  | Somente leitura
|   w  | Escrita (caso o arquivo já exista, ele será apagado e um arquivo vazio será criado)
|   a  | Leitura e escrita (adiciona o novo conteúdo ao fim do arquivo) 
|  r+  | Leitura e escrita
|  w+  | Escrita ( o modo w+, assim com o w, também apaga o conteúdo anterior do arquivo)
|  a+  | Leitura e escrita (abre o arquivo para atualização)

"""
#Abrir o arquivo
arquivo = open("arquivo.txt")

print(arquivo) # exibe as seguintes informações <_io.TextIOWrapper name='arquivo.txt' mode='r' encoding='UTF-8'>

#para mostra o conteudo do arquivo é necessário usar uma das seguintes funções
"""
read()
    - Lê arquivo inteiro
readline()
    - Lê uma linha
readlines()
    -Lê arquivo e o armazena em uma lista
"""

#pode fazer a abertura de tudo 
texto_completo = arquivo.read()
print(texto_completo)

linhas = arquivo.readlines()
print(linhas) #colocou dentro de uma lista
#para imprimir uma por uma basta usar o for
for linha in linhas:
    print(linha)

