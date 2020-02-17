# -*- coding: utf-8 -*-
# Função filter vai pegar uma determinada lista e vai filtrar uma determinada condição para ser adicionada em outra lista
# filter


def pares(i):
    if i % 2 == 0:
        return i

def impares(i):
    if i % 2 == 1:
        return i

lista = [1,2,3,4,5,6,7,8,9,10]

# pegar apenas os valores pares desta lista
lista_pares = filter(pares, lista)
print(list(lista_pares))

lista_impares = filter(impares, lista)
print(list(lista_impares))

x = [1, 2, 3]
y = [i for i in x if i % 2 == 0]
 
print(y)