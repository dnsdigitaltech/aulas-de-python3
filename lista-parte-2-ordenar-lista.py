#ordenar as listas
lista = [124,345,72,46,6,7,3,1,7,0]

#para ordenar a lista usa-se o método sort
lista.sort() # altera ardenadamente a lista que já existe
print(lista)

lista = sorted(lista) # retorno uma lista ordenada
print(lista)

#Ordenar decrescente
lista.sort(reverse=True)
print(lista)

#Inverter a lista
lista.reverse()
print(lista)

lista2 = ["bola", "abacate", "dinheiro"]
lista2.sort() #ordena a lista alfabeticamente
print(lista2)

lista2.sort(reverse=True)
print(lista2)#ordenação de strigs