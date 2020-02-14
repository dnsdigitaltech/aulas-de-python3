# Strings é um tipo de dados em que se armazena coleções de caracteres, são declaradas entre as aspas.

var1 = 1
var2 = "1" #isto é uma String

a = "Davi"

b = "Bernardo"

#Se somo duas variáveis numéricas estou somando sendo Strings estou concatenando

concatenar = a + " " + b 
print(concatenar) #unirá as duas palavras

#Saber o tamamho de uma string pela função len
tamanho = len(concatenar)
print(tamanho)#ele conta o espaço por isto 13 caracteres

#Navegação pelo indice e exibir uma determinada posição
print(a[3])#exibi o i, pois a contagem comeca com o 0, pois posição 3 é o i
print(a[0])
print(a[1])
print(a[1])
print(a[3])

#Tambem poderá imprimir um pedaço da string
print(b[0:4])#basta colocar entre colchetes o que deseja imprimir
print(b[2:0])