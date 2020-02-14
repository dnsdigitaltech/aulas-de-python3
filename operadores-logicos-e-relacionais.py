"""permite fazer comparações

==    Igual
!=    Diferente
>     Maior
<     Menor
>=    Maior ou igual
<=    Menor ou igual
"""

x = 2
y = 3



print(x == y) #False
print(x < y)  #True

soma = x + y
print(soma == x) #False
print(soma >= y) #True
print(soma = y) #False

x = y
print(x) #3