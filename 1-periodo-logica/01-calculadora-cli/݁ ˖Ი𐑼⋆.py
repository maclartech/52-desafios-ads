def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else None
def potencia(a, b): return a ** b
def modulo(a, b): return a % b if b != 0 else None

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número.")

def menu():
    print("\n CALCULADORA CLI ꉂ(˵˃ ᗜ ˂˵)")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potenciação (^)")
    print("6. Resto da divisão (%)")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o programa. Até logo!")
            break

        if opcao not in ["1", "2", "3", "4", "5", "6"]:
            print("Opção inválida! Tente novamente.")
            continue

        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        if opcao == "1":
            print(f"Resultado: {somar(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {subtrair(a, b)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcao == "4":
            resultado = dividir(a, b)
            print(f"Resultado: {resultado}" if resultado is not None else "Erro: divisão por zero!")
        elif opcao == "5":
            print(f"Resultado: {potencia(a, b)}")
        elif opcao == "6":
            resultado = modulo(a, b)
            print(f"Resultado: {resultado}" if resultado is not None else "Erro: módulo por zero!")

if __name__ == "__main__":
    main()