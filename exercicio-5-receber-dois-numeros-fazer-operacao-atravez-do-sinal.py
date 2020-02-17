# -*- coding: utf-8 -*-
# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
num1 = int(input("Digite o primeiro número: "))
operador = str(input("Digite o operador: "))
num2 = int(input("Digite o segundo numero: "))

# soma +
if operador == "+":
    resultado = num1 + num2
# subtração *
elif operador == "-":
    resultado = num1 - num2
# divisão /
elif operador == "/":
    resultado = num1 / num2
# multiplicação *
elif operador == "*":
    resultado = num1 * num2
# módulo %
elif operador == "%":
    resultado = num1 % num2
# exponenciação **
elif operador == "**":
    resultado = num1 ** num2
else:
    resultado = "Operador inválido"

print(resultado)