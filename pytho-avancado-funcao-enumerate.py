# -*- coding: utf-8 -*-
# Quando precisa navegar por um lista e obter o nome e o indice de cadas um dos elementos
lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i,lista[i]) # imprime a posição do item e o seu nome

# A melhor maneira de fazer isto e usando a função enumerate
for i, nome in enumerate(lista): # vai retornar o valor de i e nome
    print(i,nome)