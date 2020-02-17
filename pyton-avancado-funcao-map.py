# -*- coding: utf-8 -*-
# Vai pegar uma função e aplicar a todos os elementos de uma lista

def dobro(x):
    return x*2

valor = 2
print(dobro(valor)) # 4

# imagina que queremos o dobro do valor de ums lita
valor = [1,2,3,4,5]
print(dobro(valor)) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] concatena as lista e não obtem o valor da mesma

# para isto será utilizado a função map que pega cada elemeto da lista a eplica a uma determindada função
valor = [1,2,3,4,5]
valor_dobrado = map(dobro, valor) # map recebe dois argumentos
for v in valor_dobrado:
    print(v)

#converter a variavel numa lista
valor = [1,2,3,4,5]
valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado) # obtem o dobro dos valores [2, 4, 6, 8, 10]