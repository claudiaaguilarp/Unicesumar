#Estrutura condicional aninhada.

print("======Calculadora======")
print("Para soma digite 1\n"
       "Para subtrair digite 2 \n"
       "Para multiplicar digite 3 \n"
       "Para divisão digite 4")
op = int(input("Qual operação deseja? Digite o número correspondente: "))

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if op == 1:
    resultado = num1 + num2
    print(f"Resultado: {num1:.2f} + {num2:.2f} = {resultado:.2f}")
elif op == 2:
    resultado = num1 - num2
    print(f"Resultado: {num1:.2f} - {num2:.2f} = {resultado:.2f}")
elif op == 3:
    resultado = num1 * num2
    print(f"Resultado: {num1:.2f} X {num2:.2f} = {resultado:.2f}")
else: 
    if(num2 == 0):
        print("Impossível dividir por zero!")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1:.2f} / {num2:.2f} = {resultado:.2f}")