#Funções permitem as chamadas modularizações do meu códigos
#São blocos de códigos que spá serão chamados executados quando forem chamados
#Em python as funções são definidas pela palavra reservada def
"""
Definição
    def NOME(parâmetros):
        COMANDOS

Chamada
    NOME(argumentos)
"""

#Função que faz a soma de dois valores
def soma(x, y):
    print(x)
    print(y)
    print(x + y)

soma(6, 2)

#Exibir resultado fora da função é necessrio ter p return

def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

s = soma(6, 2) # é necessário cria o valor para armazenar a variavel retorno
print(s)

m = multiplicacao(3,4)
print(m)

#Também pode chamar várias funções recursivamente
print(soma(s,m))

