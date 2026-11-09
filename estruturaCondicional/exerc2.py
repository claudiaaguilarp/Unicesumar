print("=====Tabela de Preços======")
nome = input("Informe o nome do usuário do plano: ")
idade = int(input("Informe a idade do usuário do plano: "))

if idade <=18:
    mensalidade = 50
    print(f"Usuário do plano: {nome}\n"
          f"Idade: {idade} anos\n"
          f"Valor da mensalidade: R${mensalidade:.2f}")
elif idade <= 29:
    mensalidade = 70
    print(f"Usuário do plano: {nome}\n"
              f"Idade: {idade} anos\n"
              f"Valor da mensalidade: R${mensalidade:.2f}")
elif idade <= 45:
    mensalidade = 90
    print(f"Usuário do plano: {nome}\n"
          f"Idade: {idade} anos\n"
          f"Valor da mensalidade: R${mensalidade:.2f}")
elif idade <= 65:
    mensalidade = 130
    print(f"Usuário do plano: {nome}\n"
          f"Idade: {idade} anos\n"
          f"Valor da mensalidade: R${mensalidade:.2f}")
else:
    mensalidade = 170
    print(f"Usuário do plano: {nome}\n"
          f"Idade: {idade} anos\n"
          f"Valor da mensalidade: R${mensalidade:.2f}")