import java.util.Scanner;

public class e21 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    int num, sum = 0, i = 0;
    System.out.println("Dime números y los sumare (ingresa un numero negativo para finalizar)");

    do {
      System.out.print("Ingresa el número: ");
      num = sc.nextInt();
      if (num <= 0) {
        break;
      }
      sum += num;
      i++;
    } while (true);

    System.out.println("La media final es: " + (sum / i));
    sc.close();
}
}
