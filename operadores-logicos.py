"""
Permite fazer várias comparações ao mesmo tempo

AND     Duas condições sejam verdadeiras
OR      Pelo menos um condição seja verdadeira
NOT     Inverte o valor
"""

x = 2
y = 3
z = 3
o = 3
soma = x + y

print(x == y and x == soma) #False

print(y == z and o == z) #True

print(x == y and y == o) #False

print(x == y or y == o) #True