import java.util.Scanner;

public class e3 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    Scanner entrada = new Scanner(System.in);

        float plata;
        System.out.println("Cuanta plata tiene Guillermo?");
        plata = entrada.nextFloat();

        float Luis = plata / 2;
        float Juan = (plata + Luis) / 2;
        System.out.println("En ese caso, Luis tiene $"+ Luis + " y Juan tiene $"+Juan);
  }
}
