# Listas - representam consjuto de dados

"""
Pode ser
    - Numérica: [1,2,3,4,5]
    - Strings: ["bola", "sapato", "chuva"]
"""

minha_lista = ["abacaxi", "melancia", "abacate"]
print(minha_lista) # imprimirá todos elementos da lista

minha_lista2 = [1,2,3,4,5]
print(minha_lista2)

#lista mista
minha_lista3 = ["abacaxi", 2, 9.89, True]
print(minha_lista3)

#Navegação por lista
print(minha_lista[2])

#usando laço
for item in minha_lista:
    print(item)

#saber o tamanho da lista
tamanho = len(minha_lista)
print(tamanho)

#Adicionando elemento na lista usa-se o método append()
minha_lista.append("limão")
print(minha_lista)

#Verificar se o elemento pertence a lista palavra reservada in
if 7 in minha_lista2: #verificando se o numro 7 esta na lista
    print("7 está na lista")
else:
    print("7 não está na lista")

#Removendo e elemento da lista com apalavra reservada del
del minha_lista[2:]#remobendo do item 2 até o final
print(minha_lista) #removeu ["abacate", "limão"]

#Apaagar a lista inteira
del minha_lista[:]
print(minha_lista)

#criar uma lista em branco e preenchendo ela aos poucos
minha_lista4 = []
minha_lista4.append(57)
print(minha_lista4)