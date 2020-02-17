#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print ("Maior de idade")
elif idade > 0 and idade < 18:
    print ("Manor de idade")
else:
    print("Idade inválida")