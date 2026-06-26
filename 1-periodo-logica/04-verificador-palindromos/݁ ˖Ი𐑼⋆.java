import java.util.Arrays;
import java.util.Scanner;

public class VerificadorPalindromoAnagrama {

    public static String normalizar(String texto) {
        return texto.toLowerCase()
                     .replaceAll("[^a-z0-9]", "");
    }

    public static boolean isPalindromo(String texto) {
        String normalizado = normalizar(texto);
        String invertido = new StringBuilder(normalizado).reverse().toString();
        return normalizado.equals(invertido);
    }

    public static boolean isAnagrama(String texto1, String texto2) {
        char[] array1 = normalizar(texto1).toCharArray();
        char[] array2 = normalizar(texto2).toCharArray();

        if (array1.length != array2.length) {
            return false;
        }

        Arrays.sort(array1);
        Arrays.sort(array2);

        return Arrays.equals(array1, array2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n     VERIFICADOR DE PALINDROMOS E ANAGRAMAS    ");
            System.out.println("1. Verificar Palindromo");
            System.out.println("2. Verificar Anagrama");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opcao: ");

            while (!scanner.hasNextInt()) {
                System.out.print("Entrada invalida! Digite um numero: ");
                scanner.next();
            }
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1:
                    System.out.print("Digite a palavra ou frase: ");
                    String texto = scanner.nextLine();
                    if (isPalindromo(texto)) {
                        System.out.println("\"" + texto + "\" e um palindromo!");
                    } else {
                        System.out.println("\"" + texto + "\" NAO e um palindromo.");
                    }
                    break;

                case 2:
                    System.out.print("Digite a primeira palavra: ");
                    String palavra1 = scanner.nextLine();
                    System.out.print("Digite a segunda palavra: ");
                    String palavra2 = scanner.nextLine();
                    if (isAnagrama(palavra1, palavra2)) {
                        System.out.println("\"" + palavra1 + "\" e \"" + palavra2 + "\" SAO anagramas!");
                    } else {
                        System.out.println("\"" + palavra1 + "\" e \"" + palavra2 + "\" NAO sao anagramas.");
                    }
                    break;

                case 0:
                    System.out.println("Encerrando o programa. Ate logo!");
                    break;

                default:
                    System.out.println("Opcao invalida! Tente novamente.");
            }

        } while (opcao != 0);

        scanner.close();
    }
}