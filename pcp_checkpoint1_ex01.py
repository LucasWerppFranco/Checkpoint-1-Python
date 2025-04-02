reais = float(input("Insira um valor em reais: "))

escolha = input(
    "Para qual moeda você gostaria de converter o seu valor em reais\n (1) Dólar Americano\n (2) Euro\n (3) Peso Argentino\n (4) Libra Esterlina\n (5) Iene\nInsira o numero da moeda escolhida:"
)

if escolha == "1":
    dolares = round(reais / 5.68, 2)
    print(f"Seu saldo é de ${dolares} Dólares Americanos.")
elif escolha == "2":
    euros = round(reais / 6.7, 2)
    print(f"Seu saldo é de €{euros} Euros.")
elif escolha == "3":
    pesos = round(reais * 188, 2)
    print(f"Seu saldo é de ${pesos} Pesos Argentinos.")
elif escolha == "4":
    libras = round(reais / 7.40, 2)
    print(f"Seu saldo é de £ {libras} Libras Esterlinas.")
elif escolha == "5":
    ienes = round(reais * 26, 2)
    print(f"Seu saldo é de ¥ {ienes} Ienes.")
else:
    print("Por favor, adicione um numero valido")
