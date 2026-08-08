import java.util.Scanner;

public class OrdenarVisual {

  // ==========================================
  // COLORES (codigos ANSI para la terminal)
  // ==========================================
  // Esto son "escapes" que la terminal interpreta como color en vez
  // de texto normal. RESET es obligatorio ponerlo despues de cada
  // color, si no, todo lo que imprimas despues queda pintado.
  public static final String RESET = "\u001B[0m";
  public static final String AMARILLO = "\u001B[33m"; // comparando
  public static final String VERDE = "\u001B[32m"; // intercambio / ya en su lugar
  public static final String CYAN = "\u001B[36m"; // info extra
  public static final String GRIS = "\u001B[90m"; // etiquetas / texto secundario

  // Scanner global solo para poder pausar con Enter entre cada paso.
  // Lo hacemos static para no tener que pasarlo por todos los metodos.
  private static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    byte vector[] = {4, 6, 5, 3, 2, 1};

    System.out.println("=========== BURBUJA ===========");
    burbuja(vector.clone());

    System.out.println("\n=========== INSERCION ===========");
    insercion(vector.clone());

    System.out.println("\n=========== SELECCION ===========");
    seleccion(vector.clone());

    sc.close();
  }

  // ==========================================
  // METODO BURBUJA
  // ==========================================
  // La idea sigue siendo la misma: comparamos vecinos y si el de
  // la izquierda es mayor, los cambiamos de puesto. Ahora ademas
  // de mostrar el vector, explicamos en palabras que esta pasando
  // en cada linea del codigo, y esperamos que presiones Enter para
  // avanzar, como si fuera un debugger paso a paso.
  public static void burbuja(byte[] v) {
    imprimirEstado("Inicio", v, -1, -1);
    for (int i = 0; i < v.length - 1; i++) {
      for (int j = 0; j < v.length - 1 - i; j++) {
        // Esto es literalmente el "if (v[j] > v[j+1])" del codigo,
        // pero contado en palabras antes de que pase.
        System.out.println(GRIS + "  Codigo: if (v[" + j + "] > v[" + (j + 1) + "])  ->  " + v[j]
            + " > " + v[j + 1] + " ?" + RESET);
        imprimirEstado("Comparando", v, j, j + 1);

        if (v[j] > v[j + 1]) {
          System.out.println("  " + AMARILLO
              + "Si, estan desordenados -> entramos al if y los intercambiamos" + RESET);
          byte temp = v[j];
          v[j] = v[j + 1];
          v[j + 1] = temp;
          imprimirEstado("  -> Intercambio", v, j, j + 1, VERDE);
        } else {
          System.out.println("  " + CYAN
              + "No, ya estan en orden -> el if no se cumple, seguimos de largo" + RESET);
        }
        esperar();
      }
    }
    imprimirEstado("Resultado final", v, -1, -1);
  }

  // ==========================================
  // METODO ORDENAMIENTO POR INSERCION
  // ==========================================
  // Como ordenar cartas en la mano: sacamos una carta ("actual")
  // y la vamos comparando con las que ya estan ordenadas a su
  // izquierda, corriendolas de a una hasta encontrarle su lugar.
  public static void insercion(byte[] v) {
    imprimirEstado("Inicio", v, -1, -1);
    for (int i = 1; i < v.length; i++) {
      byte actual = v[i];
      int j = i - 1;

      System.out.println(GRIS + "  Codigo: actual = v[" + i + "] = " + actual
          + "   (la carta que vamos a insertar)" + RESET);
      esperar();

      while (j >= 0 && v[j] > actual) {
        System.out.println(GRIS + "  Codigo: while (v[" + j + "] > actual)  ->  " + v[j] + " > "
            + actual + " ?  Si, entonces corremos v[" + j + "] un puesto a la derecha" + RESET);
        v[j + 1] = v[j];
        j--;
        imprimirEstado("  Corriendo", v, j + 1, j + 2);
        esperar();
      }
      v[j + 1] = actual;
      System.out.println("  " + CYAN
          + "El while ya no se cumple (o llegamos al inicio) -> aca va el " + actual + RESET);
      imprimirEstado("  Insertado en su lugar", v, j + 1, -1, CYAN);
      esperar();
    }
    imprimirEstado("Resultado final", v, -1, -1);
  }

  // ==========================================
  // METODO ORDENAMIENTO POR SELECCION
  // ==========================================
  // En cada vuelta recorremos el vector buscando el numero mas
  // chico que quede, y lo vamos "seleccionando" (guardamos su
  // posicion en la variable menor). Al final de cada vuelta lo
  // mandamos al principio del tramo desordenado.
  public static void seleccion(byte[] v) {
    imprimirEstado("Inicio", v, -1, -1);
    for (int i = 0; i < v.length - 1; i++) {
      int menor = i;
      System.out.println(GRIS + "  Codigo: menor = " + i
          + "   (por ahora asumimos que este es el mas chico)" + RESET);

      for (int j = i + 1; j < v.length; j++) {
        System.out.println(GRIS + "  Codigo: if (v[" + j + "] < v[menor])  ->  " + v[j] + " < "
            + v[menor] + " ?" + RESET);
        imprimirEstado("Comparando", v, menor, j);
        if (v[j] < v[menor]) {
          menor = j;
          System.out.println(
              "  " + AMARILLO + "Si, encontramos uno mas chico -> menor ahora es la posicion "
                  + menor + " (" + v[menor] + ")" + RESET);
        } else {
          System.out
              .println("  " + CYAN + "No, el candidato actual sigue siendo el mas chico" + RESET);
        }
        esperar();
      }

      byte temp = v[i];
      v[i] = v[menor];
      v[menor] = temp;
      System.out.println("  " + VERDE
          + "Terminamos la vuelta -> mandamos el menor encontrado a la posicion " + i + RESET);
      imprimirEstado("  -> Intercambio", v, i, menor, VERDE);
      esperar();
    }
    imprimirEstado("Resultado final", v, -1, -1);
  }

  // ==========================================
  // METODO AUXILIAR PARA IMPRIMIR EL ESTADO
  // ==========================================
  // En vez de solo imprimir el vector, marcamos con [ ] las
  // posiciones "a" y "b" que se estan comparando o moviendo en
  // ese momento, y las pintamos del color que le pasemos.

  // Version corta: si no le decimos de que color pintar, usa amarillo
  // (el color por defecto para "esto se esta comparando").
  public static void imprimirEstado(String etiqueta, byte[] v, int a, int b) {
    imprimirEstado(etiqueta, v, a, b, AMARILLO);
  }

  public static void imprimirEstado(String etiqueta, byte[] v, int a, int b, String color) {
    StringBuilder sb = new StringBuilder();
    sb.append(GRIS).append(String.format("%-20s", etiqueta)).append(RESET).append(": ");
    for (int i = 0; i < v.length; i++) {
      if (i == a || i == b) {
        sb.append(color).append("[").append(v[i]).append("]").append(RESET).append(" ");
      } else {
        sb.append(" ").append(v[i]).append("  ");
      }
    }
    System.out.println(sb);
  }

  // ==========================================
  // METODO AUXILIAR PARA PAUSAR
  // ==========================================
  // Esto es lo que convierte el programa en algo "paso a paso":
  // en vez de que todo se imprima de golpe, esperamos a que el
  // usuario presione Enter antes de seguir con la siguiente linea.
  public static void esperar() {
    System.out.print(GRIS + "  [Enter para continuar] " + RESET);
    sc.nextLine();
  }
}
