import java.util.Scanner;
public class e10 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    String letra;
    Scanner entrada = new Scanner(System.in);
    System.out.println("Ingrese q para salir");
    System.out.println("dame letras y te dire si estan en mayusculas o minusculas: ");
    do{
      letra = entrada.nextLine();
      if (letra.equals(letra.toUpperCase())){

        System.out.println("la letra es mayuscula");
      }
      else if (letra.equals(letra.toLowerCase())){
        System.out.println("la letra es minuscula");
      }
      else{
        System.out.println("no es una letra");
      }
    }while (!letra.equals("q") && !letra.equals("Q"));
  }
}
