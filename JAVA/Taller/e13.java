import java.util.Scanner;

public class e13 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    Scanner sc = new Scanner(System.in);
    int horas, extra;
    float total;
    System.out.println("dime las horas que trabajaste en la semana: ");
    horas = sc.nextInt();
    if (horas > 40) {
      extra = horas - 40;
      System.out.println("trabajaste " + extra + " horas extras");
      total = 40 * 16 + extra * 20;
      System.out.println("tu pago semanal es de $" + total);
    } else {
      total = horas * 16;
      System.out.println("tu pago semanal es de $" + total);
    }
  }
}
