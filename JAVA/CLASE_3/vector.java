package CLASE_3;

public class vector {
  public static void main(String[] args) {
    int arreglos[] = {15, 38, 41, 25, 754, 134235, 3432, 32, 57, 21, 47, 19, 14, 8, 1};
    System.out.println("===== Vector Sin Ordenar =====");

    for (int arreglo : arreglos) {
      System.out.print(arreglo + ", ");
    }
    System.out.println("\n===== Vector Ordenado =====");

    for (int i = 0; i < arreglos.length; i++) {
      for (int j = 0; j < (arreglos.length - 1 - i); j++) {
        if (arreglos[j] > arreglos[j + 1]) {
          int aux = arreglos[j];
          arreglos[j] = arreglos[j + 1];
          arreglos[j + 1] = aux;

        }
      }
    }
    for (int arreglo : arreglos) {
      System.out.println(arreglo + ", ");
    }

  }
}
