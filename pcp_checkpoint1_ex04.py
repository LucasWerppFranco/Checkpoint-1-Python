def idade_em_anos_meses_dias(dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_finais = dias_restantes % 30

    return anos, meses, dias_finais


idade_dias = int(input("Digite sua idade em dias: "))

anos, meses, dias = idade_em_anos_meses_dias(idade_dias)

print(f"Você naceu dia {dias}/{meses}/{anos}.")

