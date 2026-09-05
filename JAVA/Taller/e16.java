import java.util.Scanner;
public class e16 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    int num;
    System.out
        .println("Dime números y dire si son positivos o negativos (ingresa '0' para finalizar)");

    do {
      System.out.print("Ingresa el número: ");
      num = sc.nextInt();
      if (num > 0) {
        System.out.println(num + " es positivo");
      } else if (num < 0) {
        System.out.println(num + " es negativo");
      }
    } while (num != 0);

    sc.close();
  }
}