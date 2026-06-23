def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número.")

def celsius_para_fahrenheit(c): return (c * 9/5) + 32
def fahrenheit_para_celsius(f): return (f - 32) * 5/9

def menu_temperatura():
    print("\n Conversão de Temperatura ꉂ(˵˃ ᗜ ˂˵)")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    opcao = input("Escolha: ")
    valor = ler_numero("Digite o valor: ")

    if opcao == "1":
        print(f"Resultado: {celsius_para_fahrenheit(valor):.2f} °F")
    elif opcao == "2":
        print(f"Resultado: {fahrenheit_para_celsius(valor):.2f} °C")
    else:
        print("Opção inválida!")

FATORES_DISTANCIA = {
    "metros": 1,
    "quilometros": 1000,
    "milhas": 1609.34
}

def converter_distancia(valor, origem, destino):
    valor_em_metros = valor * FATORES_DISTANCIA[origem]
    return valor_em_metros / FATORES_DISTANCIA[destino]

def menu_distancia():
    print("\n Conversão de Distância ꉂ(˵˃ ᗜ ˂˵)")
    print("Unidades disponíveis: metros, quilometros, milhas")
    origem = input("Unidade de origem: ").lower()
    destino = input("Unidade de destino: ").lower()

    if origem not in FATORES_DISTANCIA or destino not in FATORES_DISTANCIA:
        print("Unidade inválida!")
        return

    valor = ler_numero("Digite o valor: ")
    resultado = converter_distancia(valor, origem, destino)
    print(f"Resultado: {resultado:.4f} {destino}")

TAXAS_CAMBIO = {
    "USD": 1.0,
    "BRL": 5.40,
    "EUR": 0.93
}

def converter_moeda(valor, origem, destino):
    valor_em_usd = valor / TAXAS_CAMBIO[origem]
    return valor_em_usd * TAXAS_CAMBIO[destino]

def menu_moeda():
    print("\n Conversão de Moeda ꉂ(˵˃ ᗜ ˂˵)")
    print("Moedas disponíveis: USD, BRL, EUR")
    origem = input("Moeda de origem: ").upper()
    destino = input("Moeda de destino: ").upper()

    if origem not in TAXAS_CAMBIO or destino not in TAXAS_CAMBIO:
        print("Moeda inválida!")
        return

    valor = ler_numero("Digite o valor: ")
    resultado = converter_moeda(valor, origem, destino)
    print(f"Resultado: {resultado:.2f} {destino}")

def main():
    while True:
        print("\n Conversor de Unidades .✦ ݁˖")
        print("1. Temperatura")
        print("2. Distância")
        print("3. Moeda")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_temperatura()
        elif opcao == "2":
            menu_distancia()
        elif opcao == "3":
            menu_moeda()
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()