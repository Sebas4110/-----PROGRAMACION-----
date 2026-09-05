import java.util.Scanner;
public class e25 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    float [] notas = new float[10];
    float total = 0, promedio;

    System.out.println("Dime 10 notas para sacarles el promedio");
    for (byte i = 0; i < 10; i++) {
      System.out.print("Ingresa la nota " + (i + 1) + ": ");
      notas[i] = sc.nextFloat();
      total += notas[i];

    }
    promedio = total / 10;
    System.out.println("El promedio es: " + promedio);
    sc.close();

  }
}
