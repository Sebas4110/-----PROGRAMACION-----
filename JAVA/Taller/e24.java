import java.util.Scanner;

public class e24 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    int num, fact;

    System.out.println("Escribe un número y calculo su factorial: ");
    num = fact = sc.nextInt();
    sc.close();

    for (int i = num - 1; i > 0; i--) {
      fact *= i;
    }

    System.out.println(num + "! es " + fact);
  }
}