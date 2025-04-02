numero = int(input("Digite um número entre 0 e 999: "))

if 0 <= numero <= 999:
    centena = (numero // 100) * 100
    dezena = (numero % 100 // 10) * 10
    unidade = numero % 10

    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
else:
    print("Por favor, digite um número entre 0 e 999.")
