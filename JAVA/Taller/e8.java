import java.util.Scanner;

public class e8 {
  public static void main(String[] args) {
  System.out.println("Juan Esteban Ciro");
  System.out.println("Sebastián Hernandez");
  Scanner entrada = new Scanner(System.in);

      double a, b, c, x1, x2, raiz;

      System.out.println("ingrese los coeficientes de esta ecuación de segundo grado ( ax^2 + bx + c = 0)");
      System.out.println("A: ");
      a = entrada.nextDouble();
      System.out.println("B: ");
      b = entrada.nextDouble();
      System.out.println("C: ");
      c = entrada.nextDouble();

      x1 = (-b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
      x2 = (-b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);

      System.out.println("los posibles resultados con esos numeros son: x1 = "+ x1 + " y x2 = "+ x2);
    }
}
