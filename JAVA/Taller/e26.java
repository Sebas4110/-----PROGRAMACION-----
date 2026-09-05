import java.util.Scanner;

public class e26 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);

    int indice, max = 0;

    System.out.print("Ingrese la longitud deseada de la lista: ");
    indice = sc.nextInt();

    int[] lista = new int[indice];
    for (byte i = 0; i < indice; i++) {
      System.out.print("Ingrese el " + (i+1) + "° número: ");
      lista[i] = sc.nextInt();
      if (lista[i] > max) {
        max = lista[i];
      }
    }
    sc.close();

    System.out.println("El valor mas alto fue el " + max);
  }
}
 