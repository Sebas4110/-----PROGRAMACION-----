import java.util.Scanner;

public class e20 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    int num, sum = 0;
    System.out.println("Dime números y los sumare (ingresa '0' para finalizar)");

    do {
      System.out.print("Ingresa el número: ");
      num = sc.nextInt();
      sum += num;
    } while (num != 0);

    System.out.println("La suma final es: " + sum);
    sc.close();
  }
}