#compreenção de listas

x = [1,2,3,4,5]
y = [i++2 for i in x]

#adicionar apenas os numeros ímpares de x
z = [i for i in x if i%2==1]
print(z)