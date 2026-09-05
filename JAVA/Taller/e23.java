import java.util.Scanner;

public class e23 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    int num, sum = 0;
    System.out.println("Dime 10 números y los sumare");

    for (byte i = 0; i < 10; i++){
      System.out.print("Ingresa el número: ");
      num = sc.nextInt();
      sum += num;
    }
    System.out.println("La suma final es: " + sum);
    sc.close();
  }
}
