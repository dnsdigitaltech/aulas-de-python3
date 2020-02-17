# O pyton fornece um módulo chmado randon para este fim
# Com este módulo podemos chmar alguns métodos quen germa numeros aleatórios
import random

numero = random.randint(0, 10) #numeros aleatŕios de 0 a 10
print(numero)

#Existe um forma de focar a o pyton a exibir sempre o mesmo numero
random.seed(1)
numero = random.randint(0, 10) #ficará sempre em 2 e usado apenas para teste
print(numero)

#Selecionar um número aleatóriamente de uma lista
lista = [6,45,46,23,48,25]
numero = random.choice(lista) 
print(numero)