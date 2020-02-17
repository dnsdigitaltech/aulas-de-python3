# -*- coding: utf-8 -*-
# Escreva um programa que ordene uma lista numérica com três elementos.  

"""lista = [3,2,1]

lista = sorted(lista)

print(lista)"""

#Algoritimos de complexidade com select sort

lista = [500,2,3,9,23,70,3,2,1]

#primeiro fazer uma iteração
for i in range(len(lista)): #analizar elemento por elemento
    menor = i #variavel auxiliar
    for j in range(i+1, len(lista)): #comparar o menor elemento com todos os outros
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i] # alterar o valor da primeira posição
        lista[i] = lista[menor] # o primiero elemento receberá o menor elemento
        lista[menor] = aux #inverteo
print(lista)
