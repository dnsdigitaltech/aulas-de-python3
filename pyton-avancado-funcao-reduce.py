# Função reduce - recebe uma lista e retona umunico valor apra esta lista, usamos para obter a soma dos valores de uma lista
from functools import reduce

def soma (x,y):
    return x+y

lista = [1,3,5,10,20]

#obter a soma dos valores
soma = reduce(soma, lista)
print(soma)