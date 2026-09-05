import java.util.Scanner;
public class e12 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    int valor, total;
    Scanner sc = new Scanner(System.in);
    System.out.print("cuanto es el valor de tu compra? ");
    valor = sc.nextInt();
    if (valor >= 300 ){
      System.out.println("Tienes un descuento del 20%");
      total = valor - (valor * 20 / 100);
      System.out.println("El coste seria en total $"+total);
    }else {
      System.out.println("no existe descuento, por ende, el total seria $"+ valor);
    }
   }
 }

