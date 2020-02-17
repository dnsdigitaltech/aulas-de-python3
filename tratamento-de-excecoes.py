#A medida que seu sistema vai crescendo tem certas particularidades que não tem como você testa, 
# então é necessário tratar as excessões
a = 2
b = 2
print(a/b) #funionou perfeitamente

#fazendo uma divisão por 0 dar erro, pois não podemos fazer divisão por 0, então vamos tratar este erro
# Para resoçver este problema é necessário usar o conceito de tratamento de excessões
a = 3
b = 0

try:
    print(a/b)

except:
    print("Não é permitida divisão por 0")

print(a/a) #conseguimos dividir pois o erro snterior for tratado