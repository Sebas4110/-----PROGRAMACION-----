import java.util.Scanner;

public class e28 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);

    int[] tabla1 = new int[10];
    int[] tabla2 = new int[10];
    int[] tabla3 = new int[20];

    System.out.println("Introduce 10 números enteros para la tabla 1:");
    for (int i = 0; i < 10; i++) {
      System.out.print("Número " + (i + 1) + ": ");
      tabla1[i] = sc.nextInt();
    }

    System.out.println("\nIntroduce 10 números enteros para la tabla 2:");
    for (int i = 0; i < 10; i++) {
      System.out.print("Número " + (i + 1) + ": ");
      tabla2[i] = sc.nextInt();
    }

    for (int i = 0; i < 10; i++) {
      tabla3[i * 2] = tabla1[i];
      tabla3[i * 2 + 1] = tabla2[i];
    }

    System.out.println("\nTabla 1:");
    for (int i = 0; i < 10; i++) {
      System.out.print(tabla1[i] + " ");
    }

    System.out.println("\nTabla 2:");
    for (int i = 0; i < 10; i++) {
      System.out.print(tabla2[i] + " ");
    }

    System.out.println("\nTabla 3 mezclada");
    for (int i = 0; i < 20; i++) {
      System.out.print(tabla3[i] + " ");
    }

    sc.close();
  }
}