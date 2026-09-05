import java.util.Scanner;

public class e5 {
  public static void main(String[] args) {
    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
     Scanner entrada = new Scanner(System.in);

        float nota1, nota2, nota3, nota4;
        System.out.println("dime tus 4 notas del semestre para promediar");
        System.out.print("participación: ");
        nota1 = entrada.nextFloat();
        System.out.print("primer examen parcial: ");
        nota2 = entrada.nextFloat();
        System.out.print("segundo examen parcial: ");
        nota3 = entrada.nextFloat();
        System.out.print("examen final: ");
        nota4 = entrada.nextFloat();

        float promedio = (nota1 * 0.10f) + (nota2 * 0.25f) + (nota3 * 0.25f) + (nota4 * 0.40f);
        System.out.println("tu promedio del semestre fue de " + promedio);
  }
}
