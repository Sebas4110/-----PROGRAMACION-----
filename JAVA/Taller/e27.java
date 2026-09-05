import java.util.Scanner;

public class e27 {

  public static void main(String[] args) {
    final int tamaño = 10;
    int[] numeros = new int[tamaño];
    Scanner sc = new Scanner(System.in);

    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");
    for (int i = 0; i < tamaño; i++) {
      System.out.print("Ingrese el número " + (i + 1) + ": ");
      numeros[i] = sc.nextInt();
    }
    sc.close();


    System.out.println("\nOrden intercalado (extremos hacia el centro):");
    intercalado(numeros);
  }


  public static void intercalado(int[] arreglo) {
    int izquierda = 0, derecha;
    derecha = arreglo.length - 1;

    while (izquierda < derecha) {
      System.out.println(arreglo[izquierda]);
      System.out.println(arreglo[derecha]);
      izquierda++;
      derecha--;
    }

    if (izquierda == derecha) {
      System.out.println(arreglo[izquierda]);

    }
  }

}
