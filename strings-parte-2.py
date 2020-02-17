# -*- coding: utf-8 -*-
# Em python strings sãp objets, podendo-se aplicar métodos a stringd
#string = string.método()

var1 = 1
var2 = "1" #isto é uma String

a = "Davi"

b = "Bernardo"

concatenar = a + " " + b
print(concatenar)

#alterar a caixa no nossa string deixando tudo em minúsculo
print(concatenar.lower()) # É obrigatŕio este parentese

#alterar a caixa no nossa string deixando tudo em maiúsculo
print(concatenar.upper())

# Função strip - remova tanto espacos quanto caracteres especiais nos final da strings
concatenar = a + " " + b + "\n"
print(concatenar) # ao imprimir dar uma quebra de linha
print(concatenar.strip()) # remove o a quebra de linha ou espaços

# Função split - converte a sequência em uma lista
minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r") #['O ', 'ato ', 'oeu a ', 'oupa do ', 'ei de Roma']
print(minha_lista)

# Função dind - faz buscas de sub-strings (pedados da minha strings)
# que posção aparece a palavra 'rei'
busca = minha_string.find("rei")
print(busca)# indice 23
print(minha_string[busca:])# imprime os caracteres depois de rei 'rei de Roma'
# o que acontece se não encontrar a string
busca = minha_string.find("rainha")
print(busca) # retorna o valor -1

#Função replace() - substitui parte de ums strings
minha_string  = minha_string.replace("o rei", "a rainha")
print(minha_string)
