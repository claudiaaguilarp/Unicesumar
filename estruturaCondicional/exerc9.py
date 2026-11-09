print("Código de funcionários\n"
      "1 - Servente\n"
      "2 - Pedreiro\n"
      "3- Mestre de Obras\n"
      "4- Técnico de Segurança")

cod = int(input("Informe o código do funcionário: "))
salario = float(input("Informe o salário: "))

if cod == 1:
    aumento = salario* 0.40
    salarioFinal = salario + aumento
    print(f"O salário do Servente teve um aumento de R$ {aumento:.2f}, sendo assim seu novo salário será R$ {salarioFinal:.2f}")
elif cod == 2:
    aumento = salario* 0.35
    salarioFinal = salario + aumento
    print(f"O salário do Pedreiro teve um aumento de R$ {aumento:.2f}, sendo assim seu novo salárioserá R$ {salarioFinal:.2f}")
elif cod == 3:
    aumento = salario* 0.20
    salarioFinal = salario + aumento
    print(f"O salário do Mestre de Obras teve um aumento de R$ {aumento:.2f}, sendo assim seu novo salárioserá R$ {salarioFinal:.2f}")
else:
    aumento = salario* 0.10
    salarioFinal = salario + aumento
    print(f"O salário do Técnico de Segurança teve um aumento de R$ {aumento:.2f}, sendo assim seu novo salárioserá R$ {salarioFinal:.2f}")