# Exercicio 1
while True:
    try:
        num1 = int(input("digite um número inteiro: "))
        break
    except ValueError:
        print("ERRO: Digite um número intiro válido!")

# Exercício 2
while True:
    try:
        num1 = int(input("digite outro número inteiro: "))
        if  num1 < 0:
            print("O número não pode ser negativo!")
            continue
        else:
            break
    except ValueError:
        print("ERRO: O número não pode conter letras e/ou pontos!")

#-----------------------------------------------------------------
# Exercício 3
while True:   
    try:
        idade1 = int(input("Digite sua idade: "))
        if idade1 > 0 and idade1 <= 120:
            print("Idade válida")
            break
        else:
            print("A idade precisa ser entre 0 e 120!")
            continue
    except ValueError:
        print("ERRO: A idade não pode conter letras e/ou pontos!")
        continue
    
#-----------------------------------------------------------------
# Exercício 4 
while True:
    try:
        nota1 = float(input("digite uma nota de zero a dez: "))
        if nota1 > 0 and nota1 <= 10:
            print("Nota válida.")
            break
        else:
            print("A nota precisa ser entre zero e dez!")
            continue
    except ValueError:
        print("ERRO: A nota não pode conter letras!")
        continue

#-----------------------------------------------------------------
'''nível 2 — Lógica com operadores'''
# Exercício 5
while True:
    try:
        num2 = int(input("Digite um valor inteiro: "))
        if num2 % 2 == 0:
            print("É par.")
        else:
            print("É ímpar")
    except ValueError:
        print("ERRO: O valor não pode conter letras!")
        break

#-----------------------------------------------------------------
# Exercício 6
while True:
    try:
        idade2 = int(input("digiite sua idade: "))
        if idade2 >= 18 and idade2 <= 65:
            print("Idade válida.")
            break
        else:
            print("idade inválida, a idade precisa ser entre 18 e 65 anos")
            continue            
    except ValueError:
        print("ERRO: Digite uma idade válida!")

#-----------------------------------------------------------------
# Exercício 7
while True:
    try:
        idade3 = int(input("Digite sua idade: "))
        if idade3 >= 12 and idade3 <= 60:
            print("Idade válida.")
            break
        else:
            print("A idade precisa ser entre 12 e 60 anos")
            continue
    except ValueError:
        print("ERRO: A idade não pode conter letras e/ou vírgulas!")

#-----------------------------------------------------------------
# Exercício 8
while True:
    try:
        print("Crie uma senha de quatro dígitos.")
        senha1 = int(input("Ela deve ser um número entre '1000' e '9999': "))
        if senha1 >= 1000 and senha1 <= 9999:
            print("Senha válida.")
            break
        else:
            print("A senha precisa ser entre '1000' e '9999'! ")
            continue
    except ValueError:
        print("ERRO: Sua senha não pode conter letras e/ou símbolos!")

'''Nível 3 — Validação realista'''
#-----------------------------------------------------------------
# Exercício 9
while True:
    try:
        print("O valor salarial deve estar compreendido entre R$ 1.320,00 e R$ 50.000,00.")
        salario1 = float(input("Digite sua faixa salárial: "))
        if 1320 <= salario1 <= 50000:
            print("salário válido")
            break
        else:
            print("O valor precisa estar entre R$ 1.320,00 e R$ 50.000,00!")
            continue
    except ValueError:
        print("ERRO: não pode conter letras!")

#-----------------------------------------------------------------
# Exercício 10
while True:
    try:
        pecas1 = int(input("Qual a quantidade de peças armazenadas? "))
        if pecas1 < 0:
            print("valor incorreto, não pode ser menor do que zero!") 
            continue
        elif pecas1 > 1000:
            print("valor de peças no estoque excedido, armazenar em outro local!")
            continue
        else:
            print("Quantidade de peças conforme o parâmetro.")
            break
    except ValueError:
        print("ERRO: não pode conter letras!")

#-----------------------------------------------------------------
# Exercício 11
