print("Caixa Eletrônico")

valor = int(input("Valor do saque: "))


if valor <= 0 or valor % 10 != 0:
    print("Valor inválido. O saque deve ser múltiplo de 10.")
else:
    
    notas_100 = valor // 100
    resto = valor % 100

    notas_50 = resto // 50
    resto = resto % 50

    notas_10 = resto // 10

    
    print(f"Notas de 100 USD: {notas_100}")
    print(f"Notas de 50 USD: {notas_50}")
    print(f"Notas de 10 USD: {notas_10}")
