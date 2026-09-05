import java.util.Scanner;

public class e6 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
      Scanner entrada = new Scanner(System.in);

        double num1, num2, poten1, poten2, expo = 2, resultado;
        System.out.println("dame dos numeros para resolver el cuadrado de la suma (a+b)^2");
        num1 = entrada.nextDouble();
        num2 = entrada.nextDouble();

        poten1 = Math.pow(num1, expo);
        poten2 = Math.pow(num2, expo);
        resultado = (poten1) + 2*(num1 + num2) + (poten2);

        System.out.println("el resultado es "+ resultado);
  }
}