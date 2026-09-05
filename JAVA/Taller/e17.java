import java.util.Scanner;

public class e17 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");
    Scanner sc = new Scanner(System.in);
    int num;

    do {
      System.out.println("Ingrese 0 para salir");
      System.out.println("dame un numero y te dire si es par o impar: ");
      num = sc.nextInt();
      if (num %2 == 0 & num != 0) {
        System.out.println("El numero es par");
      } else if (num == 0) {
        System.out.println("el numero es cero");
      } else if (num %2 != 0) {
        System.out.println("El numero es impar");
      }
    } while (num != 0);
    System.out.println("hasta luego");
  }

  }
