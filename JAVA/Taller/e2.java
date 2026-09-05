package Taller;

import java.util.Scanner;

public class e2 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
      float horas, salario;
      System.out.println("dime tus horas trabajadas: ");
      System.out.print("Horas trabajadas: ");
      horas = entrada.nextFloat();

      System.out.println("dime tu salario por hora:");
      System.out.print("Salario por hora: ");
      salario = entrada.nextFloat();

      float total = salario * horas;

      System.out.println("tu salario semanal es de "+ total);
  }
}
