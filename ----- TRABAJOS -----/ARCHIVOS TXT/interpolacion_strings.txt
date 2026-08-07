package Tecnica.POO_modulo_2.Java.Clase_13;

public class interpolacion_strings {
  public static void main(String[] args) {
    // ========== SOLO CONSOLA ==========
    // System.out.printf(formato, valores)
    System.out.printf("%s tiene %d años", "Ciro", 15);

    // ========== GUARDAR VALORES ==========
    // String.format(formato, valores)

    // ----- ENTEROS (%d) -----
    String resultado1 = String.format("%d - %d - %d", 10, 20, 30);
    System.out.println(resultado1);

    // ----- STRING (%s) -----
    String nombre = "Codi";
    String apellido = "Facilito";

    String nombreCompleto = String.format("%s %s", nombre, apellido);
    System.out.println(nombreCompleto);

    // ----- FLOAT (%f) -----
    final float pi = 3.14159265359f;
    String resultado2 = String.format("%f - Decimales: %.2f", pi, pi);
    System.out.println(resultado2);

    // ----- BOOLEAN (%b) -----
    int cantidad = 10;
    boolean mayor = cantidad > 5;
    String resultado3 = String.format("La cantidad es mayor a %d : %b",
        cantidad, mayor);
    System.out.println(resultado3);

    // ========== ORDEN ==========
    // El reemplazo de los valores es lineal, sin embargo, habrá ocasiones en las
    // cuales nosotros necesitemos especificar el orden, en esos casos seguiremos la
    // siguiente estructura %, posición, $, tipo

    String uno = "Uno";
    String dos = "Dos";
    String tres = "Tres";
    String resultado4 = String.format("%3$s - %2$s - %1$s",
        uno, dos, tres);
    System.out.println(resultado4);

    String resultado5 = String.format("%1f - Decimales: %1$.2f", pi, pi);
    System.out.println(resultado5);
  }
}
