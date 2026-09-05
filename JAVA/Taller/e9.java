import java.util.Scanner;
public class e9 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    int num1 = 0, num2 = 0;
    int mayor = 0;
    Scanner entrada = new Scanner(System.in);
    System.out.println("dame dos numeros y te dire cual es el mayor");
    System.out.print("dame el primer numero: ");
    num1 = entrada.nextInt();
    System.out.print("dame el segundo numero: ");
    num2 = entrada.nextInt();

    if (num1 > num2) {
      mayor = num1;
    } else if (num2 > num1) {
      mayor = num2;
    }
    System.out.println("el numero mayor es: " + mayor);
  }
}
