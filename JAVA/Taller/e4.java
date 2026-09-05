import java.util.Scanner;

public class e4 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    Scanner entrada = new Scanner(System.in);

        int costo, cantidad;
        int comisión = 150;
        System.out.println("cuantos carros vendio en el mes?");
        cantidad = entrada.nextInt();
        System.out.println("de que valor eran los carros?");
        costo = entrada.nextInt();

        float comision = comisión * cantidad;
        float porcen = costo * 0.05f;

        float ganancia = 1000 + porcen + comision;
        System.out.println("la ganancia de este mes fue de $"+ ganancia);
  }
}
