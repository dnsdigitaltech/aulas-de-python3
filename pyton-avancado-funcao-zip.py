
# -*- coding: utf-8 -*-
# Imprimir dois valores de duas listas diferentes concatenando os elementos, a função zip compactará estas duas listas como se fosse uma para usarmos

lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro"]
lista3 = ["R$ 2,00", "R$ 5,00", "Não tem preço", "Não tem preço", "Não tem preço"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)