def balada_do_joca():
    """Simula o processo de entrada na Balada do joca."""

    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Liberado para entrar!")
    elif idade >= 16:
        autorizacao_pais = input("Autorização dos pais (S/N)? ").upper()
        if autorizacao_pais == "S":
            print("Liberado para entrar!")
        else:
            print("Não está liberado para entrar.")
    else:
        print("Não está liberado para entrar.")

# Executa a função
balada_do_joca ()*-63