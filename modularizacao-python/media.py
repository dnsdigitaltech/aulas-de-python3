# Calcular 3 funções média, mediana, moda
# media - soma e divide por toral de elementos
# mediana - ordenar todos os numeros da lista e pegar o que está no meio, se tem um total de numeors pares na lista pega os dois do meio e calcula a média entre eles
# moda - simplemente o valor que mais se repete na lista

# Modo fácil usando bibliotes do python

from statistics import *
"""
# calcular a média do modo fácil
mean(lista)

# calcular a mediana
median(lista)

# calcular a moda
mode(lista)
"""

# Vamos fazer do jeito difícil, calcular manual
def media(lista):
    media = sum(lista)/float(len(lista))

    return media

def mediana(lista):
    # return median(lista)
    # primeiro teremos que ordanar a lista
    lista_ordenada = sorted(lista)
    t = len(lista_ordenada)
    # para calcular a media tera que saber se a lista é par ou impar
    if t % 2 == 0: # par
        mediana = (lista_ordenada[int(t/2)]+lista_ordenada[int((t/2)-1)])/2 # somar os dois numero do meio e dividir por 2
    elif t % 2 == 1: # impar
        mediana = lista_ordenada[int((t/2))]
    
    return mediana

def moda(lista):
    # o numero que mais repete na lista, então usaremos o dicionario para receber todos os numeros da lista
    # e decidir qual o maior elemento que mais se repete
    lista_dic = {}
    # percorrer a lista
    for l in lista:
        # verificar se o elemento não esta no dicionário e insere
        if l not in lista_dic:
            lista_dic[l] = 1
        else:
            # ver valores que se repetem e soma + 1
            lista_dic[l] += 1
        
    # pegar maior de repetição da lista
    maior_repeticao = max(lista_dic.values())
    # pegar o indice do elemento que mais se repete
    for i in lista_dic:
        # verifica se elemento é igual ao meu valor
        if lista_dic[i] == maior_repeticao:
            moda = i

    return moda