def conversao_de_moedas(reais):
    escolha = input(
        "Para qual moeda você gostaria de converter o seu valor em reais\n (1) Dólar Americano\n (2) Euro\n (3) Peso Argentino\n (4) Libra Esterlina\n (5) Iene\nInsira o numero da moeda escolhida: "
    )

    if escolha == "1":
        moeda = round(reais * 0.18)
        icone = "$"
    elif escolha == "2":
        moeda = round(reais * 0.16)
        icone = "€"
    elif escolha == "3":
        moeda = round(reais * 190.83)
        icone = "ARS"
    elif escolha == "4":
        moeda = round(reais * 0.14)
        icone = "£"
    elif escolha == "5":
        moeda = round(reais * 25.79)
        icone = "¥"
    else:
        print("Por favor, adicione um numero valido")
        return None, None

    return moeda, icone


try:
    reais = float(input("Insira um valor em Reais: "))
    moeda, icone = conversao_de_moedas(reais)
    if moeda is not None and icone is not None:
        print(f"Seu saldo é de {icone}{moeda}")
except ValueError:
    print("Por favor, Insira um valor valido")
