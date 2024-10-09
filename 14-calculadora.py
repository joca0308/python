def inicio():
    while True:
        print("## CALCULADORA ##\n")
        print("1. soma")
        print("2. subtração")
        print("3. multiplicação")
        print("4. divisão")
        print("5. resto da divisão")
        print("6. sair")
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 6:
            print("saindo...")
            break
        
        num1 = float(input("digite o primeiro valor: "))
        num2 = float(input("digite o segundo valor: "))
        
        if opcao == 1:
            resultado = num1 + num2
            print("a soma dos valores:", resultado, "\n")
        elif opcao == 2:
            resultado = num1 - num2
            print("a subtração dos valores:", resultado)
        elif opcao == 3:
            resultado = num1 * num2
            print("a multiplicação dos valores:", resultado)
        elif opcao == 4:
            resultado = num1 / num2
            print("a divisão dos valores:", resultado)
        elif opcao == 5:
            resultado = num1 % num2
            print("o resto da divisão dos valores:", resultado)
        else:
            print("opção inválida, tente novamente.")

inicio()
