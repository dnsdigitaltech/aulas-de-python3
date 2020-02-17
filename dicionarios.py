# Dicionários são lista de associações compostas por:

"""
 - uma chave
 - um valor correspondente

    dicionario = {CHAVE:valor}
"""

#OBS: A lista é declarada entre [], já o dicionário é declarado entre {}, só que usa-se [] para buscar valores

meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C": "CACHORRO"}

#Imprimir a primeira posição do dicionário
#print(meu_dicionario[0])#errado, pois não é lista, não é por localização, não tem uma ordem correta no dicionário
print(meu_dicionario["A"]) #para imprimir a posição basta chmar a chave, neste caso é A

#Imprimir o dicionário inteiro
print(meu_dicionario) #{'A': 'AMEIXA', 'B': 'BOLA', 'C': 'CACHORRO'}

#Navegando pelo dicionário
for chave in meu_dicionario:
    print(chave + ":" + meu_dicionario[chave])

#Usando funções
#items() - retorna todos os itens do dicionário
for i in meu_dicionario.items():
    print(i) # converte o dicionário em um tupla (conjuto de dados que são imutáveis)

#values() - retorna apenas os valores do dicionário
for i in meu_dicionario.values():
    print(i)

#keys() - retorna apenas as chaves do dicionário
for i in meu_dicionario.keys():
    print(i)