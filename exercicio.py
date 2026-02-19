while True:
    try:  
        nome = str(input("Digite seu nome e sobrenome: "))
        checknum = any(num.isdigit() for num in nome)
        print (checknum)
        if " " in nome and not checknum:
            print("Nome válido e sem números!")
        elif checknum:
            print("Erro: Nomes não devem conter números.")
        else:
            print("Erro: Por favor, digite seu nome e sobrenome.")

    except ValueError:
        print("erro")
    try:
        idade = int(input("Digite a sua idade: "))
        if idade <= 0 or idade >= 130:
            print("Erro: Idade inválida, por favor digite sua idade corretamente. ")
        else:
            print("idade válida")   

    except ValueError:
        print("erro")

    try:
        salario = float(input("Digite o valor do salário que você recebe: "))
        if salario < 0:
            print("Erro: Valor incorreto, digite o valor que recebe, não o que deve! ")
        else:
            print("Valor válido.")

    except ValueError:
        print("erro")

    try:
        usuario = str(input("Digite o nome de usuário: ")) 
        senha = int(input("Digite a senha: "))
        if usuario == "admin" and senha == 123:
            print ("Senha e usuário corretos.")
            break
        else:
            print("senha e/ou usuários incorretos, favor tente novamente!")


    except ValueError:
        print("erro")