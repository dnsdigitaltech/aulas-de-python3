# Caso a condição possua mais de uma comparação tabulada, executa a primeira condição verdadeira que existe
# y > x, porém ele executou x < y, pois foi a primeira opção verdadeira
# -*- coding: utf-8 -*-
x = 1
y = 2

if x == y:
    print("Números iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("Números diferentes")