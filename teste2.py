while True:
        def soma(a, b):
            return(a + b)
        def sub(a, b):
            return(a - b)
        def mult(a, b):
            return(a * b)
        def div(a, b):
            return(a / b)
        
        
        n1 = int(input('escreva um numero: '))
        ope = (input("digite uma função: "))
        n2 = int(input('escreva outro numero: '))
        
        if ope == "+":
            print ('Resultado: ', soma(n1, n2))
        elif ope == "-":
            print ('Resultado: ', sub(n1, n2))
        elif ope == "*":
            print ('Resultado: ', mult(n1, n2))
        elif ope == "/":
            print ('Resultado: ', div(n1, n2))
        
        sair = input("deseja continuar? (sim/não): ")
        if sair == "não":
            break 