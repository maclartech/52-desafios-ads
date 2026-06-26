// Caixas eletrônicos precisam decidir, de forma eficiente, quantas cédulas de cada valor entregar para um saque,
// minimizando a quantidade total de notas. O desafio era criar um programa em C que recebesse
// um valor de saque e calculasse a distribuição de cédulas de $50, $20, $10 e $1, utilizando divisão inteira e operador de módulo.

#include <stdio.h>

int main()
{
    int valor, valorOriginal;
    int cedulas[] = {50, 20, 10, 1};
    int quantidades[4] = {0, 0, 0, 0};
    int tamanho = 4;

    printf("     CAIXA ELETRONICO     \n");
    printf("Digite o valor do saque: ");
    scanf("%d", &valor);

    if (valor <= 0)
    {
        printf("Valor invalido! O saque deve ser positivo.\n");
        return 1;
    }

    valorOriginal = valor;

    for (int i = 0; i < tamanho; i++)
    {
        quantidades[i] = valor / cedulas[i];
        valor = valor % cedulas[i];
    }

    printf("\nSaque de $%d sera entregue da seguinte forma:\n", valorOriginal);
    for (int i = 0; i < tamanho; i++)
    {
        if (quantidades[i] > 0)
        {
            printf("- %d nota(s) de $%d\n", quantidades[i], cedulas[i]);
        }
    }

    if (valor > 0)
    {
        printf("\nAtencao: nao foi possivel entregar $%d restante com as cedulas disponiveis.\n", valor);
    }

    return 0;
}