package JAVA.Taller;
import java.util.Scanner;
public class e15 {

  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernández");
    Scanner sc = new Scanner(System.in);
    int num1, num2, suma, resta, multi, divi;

    System.out.println("===== BIENVENIDO =====");
    System.out.println("¿Qué desea hacer?\n" +
        "Suma (S o s)\n" +
        "Resta (R o r)\n" +
        "Multiplicación (M o m)\n" +
        "División (D o d)");
        String op = sc.nextLine();
    switch (op) {
      case "S":
      case "s":
        System.out.println("Ingrese el primer numero: ");
        num1 = sc.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        num2 = sc.nextInt();
        suma = num1 + num2;
        System.out.println("El resultado de la suma es: " + suma);
        break;
      case "R":
      case "r":
        System.out.println("Ingrese el primer numero: ");
        num1 = sc.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        num2 = sc.nextInt();
        resta = num1 - num2;
        System.out.println("El resultado de la resta es: " + resta);
        break;
      case "M":
      case "m":
        System.out.println("Ingrese el primer numero: ");
        num1 = sc.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        num2 = sc.nextInt();
        multi = num1 * num2;
        System.out.println("El resultado de la resta es: " + multi);
        break;
      case "D":
      case "d":
        System.out.println("Ingrese el primer numero: ");
        num1 = sc.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        num2 = sc.nextInt();
        divi = num1 / num2;
        System.out.println("El resultado de la resta es: " + divi);
        break;
      default:
        System.out.println("Numero incorrecto o nulo");
        System.out.println("Intentelo nuevamente");
    }

  }

  }
