public class ordenar {
  public static void main(String[] args) {
    byte vector[] = {4, 6, 5, 3, 2, 1};

    // METODO BURBUJA
    burbuja(vector.clone());

    // METODO ORDENAMIENTO POR INSERCION
    insercion(vector.clone());

    // METODO ORDENAMIENTO POR SELECCION
    seleccion(vector.clone());
  }

  // ==========================================
  // METODO BURBUJA
  // ==========================================
  // La idea es simple: comparamos elementos vecinos,
  // y si el de la izquierda es mayor que el de la derecha,
  // los intercambiamos. Así, en cada vuelta, el número más
  // grande "burbujea" hacia el final del vector, como una
  // burbuja subiendo en el agua.
  public static void burbuja(byte[] v) {
    for (int i = 0; i < v.length - 1; i++) {
      // Cada vuelta "empuja" el mayor hacia el final
      for (int j = 0; j < v.length - 1 - i; j++) {
        if (v[j] > v[j + 1]) {
          // Intercambiamos si están desordenados
          byte temp = v[j];
          v[j] = v[j + 1];
          v[j + 1] = temp;
        }
      }
    }
    imprimir("Burbuja", v);
  }

  // ==========================================
  // METODO ORDENAMIENTO POR INSERCION
  // ==========================================
  // Es como cuando ordenas cartas en la mano: agarras una carta
  // y la vas metiendo en el lugar correcto entre las que ya
  // tenías ordenadas. Vamos tomando cada número y lo insertamos
  // en su posición correcta entre los ya ordenados.
  public static void insercion(byte[] v) {
    for (int i = 1; i < v.length; i++) {
      byte actual = v[i]; // el numero que vamos a "insertar"
      int j = i - 1;

      // Movemos los elementos mayores una posicion a la derecha
      while (j >= 0 && v[j] > actual) {
        v[j + 1] = v[j];
        j--;
      }
      // Aca insertamos el numero en su lugar correcto
      v[j + 1] = actual;
    }
    imprimir("Insercion", v);
  }

  // ==========================================
  // METODO ORDENAMIENTO POR SELECCION
  // ==========================================
  // Buscamos el numero mas chico de todo el vector y lo mandamos
  // al principio. Después buscamos el segundo mas chico y lo
  // mandamos a la segunda posicion, y asi sucesivamente, como
  // "seleccionando" el mejor candidato en cada vuelta.
  /*
   * public static void seleccion(byte[] v) { for (int i = 0; i < v.length - 1; i++) { int menor =
   * i; // asumimos que este es el menor
   *
   * for (int j = i + 1; j < v.length; j++) { if (v[j] < v[menor]) { menor = j; // encontramos uno
   * mas chico, actualizamos } }
   *
   * // Intercambiamos el menor encontrado con la posicion actual byte temp = v[i]; v[i] = v[menor];
   * v[menor] = temp; } imprimir("Seleccion", v); }
   *
   * // Metodo auxiliar solo para imprimir bonito public static void imprimir(String nombre, byte[]
   * v) { System.out.print(nombre + ": "); for (byte b : v) { System.out.print(b + " "); }
   * System.out.println();
   */
}
