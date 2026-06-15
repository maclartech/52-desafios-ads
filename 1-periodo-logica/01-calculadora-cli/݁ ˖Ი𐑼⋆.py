# Precisei voltar a treinar lógica condicional, laços de repetição e manipulação de entrada/saída antes de mergulhar em estruturas mais complexas. 
# O desafio era criar uma calculadora de linha de comando que fosse além das quatro operações básicas, incluindo potenciação e resto da divisão,
# com um menu interativo que permitisse ao usuário realizar várias operações sem precisar reiniciar o programa a cada cálculo.

import os

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
            print("Entrada inválida! Digite um número válido.")

def menu():
    print("\n    CALCULADORA CLI ꉂ(˵˃ ᗜ ˂˵)       ")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potenciação (^)")
    print("6. Resto da divisão (%)")
    print("M. Zerar Calculadora")
    print("0. Sair do Programa")
    print("────୨ৎ────────୨ৎ────────୨ৎ────")

def main():
    resultado_anterior = None
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "0":
            print("Até logo! ◝(ᵔᗜᵔ)◜")
            break
            
        if opcao == "M":
            resultado_anterior = None
            os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
            print("Memória zerada! Começando novos cálculos. (*ᴗ͈ˬᴗ͈)ꕤ*.ﾟ")
            continue

        if opcao not in ["1", "2", "3", "4", "5", "6"]:
            print("Opção inválida! Tente novamente.")
            continue

        if resultado_anterior is None:
            a = ler_numero("Digite o primeiro número: ")
        else:
            a = resultado_anterior
            print(f"➜ Número atual (da conta anterior): {a}")

        b = ler_numero("Digite o segundo número: ")
        resultado = None
        if opcao == "1":
            resultado = somar(a, b)
        elif opcao == "2":
            resultado = subtrair(a, b)
        elif opcao == "3":
            resultado = multiplicar(a, b)
        elif opcao == "4":
            resultado = dividir(a, b)
            if resultado is None:
                print("Erro: Não é possível dividir por zero!")
        elif opcao == "5":
            resultado = potencia(a, b)
        elif opcao == "6":
            resultado = modulo(a, b)
            if resultado is None:
                print("Erro: Não é possível calcular o resto por zero!")
        if resultado is not None:
            print(f"Resultado: {resultado}")
            resultado_anterior = resultado
        else:
            resultado_anterior = None 

if __name__ == "__main__":
    main()