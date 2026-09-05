import java.util.Scanner;

public class e7 {
public static void main(String[] args) {
  System.out.println("Juan Esteban Ciro");
  System.out.println("Sebastián Hernandez");
  Scanner entrada = new Scanner(System.in);
        int horas;
        System.out.println("dame un numero de horas y lo convertire en dias, semanas y horas sobrantes");
        horas = entrada.nextInt();
        int semanas, dias, horas2;
        semanas = horas / 168;
        dias = (horas % 168) / 24;
        horas2 = (horas % 168) % 24;
        System.out.println("la comversión seria igual a: "+ semanas+" semanas, "+ dias +" dias y "+ horas2 + " horas");
  }
}
