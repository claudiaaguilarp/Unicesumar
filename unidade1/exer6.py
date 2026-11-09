#Escreva um programa que receba dois números, calcule e apresente o resultado do primeiro número elevado ao segundo.
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

elevado = num1**num2
print(f"{num1} elevado a {num2} é igual a: {elevado:.2f}")