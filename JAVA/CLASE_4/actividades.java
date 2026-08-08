import java.util.Scanner;
import javax.swing.JOptionPane;

public class actividades {
  public static void actividad_15_16() {
    Scanner entrada = new Scanner(System.in);
    int nFilas, nColumnas, matrizA[][], matrizB[][];
    boolean cuadrada, esTraspuesta;

    // CREAR MATRIZ
    nFilas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de filas:"));
    nColumnas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de columnas:"));
    matrizA = new int[nFilas][nColumnas];
    matrizB = new int[nColumnas][nFilas];
    System.out.println("Escriba cada elemento de la matriz despues del enter");

    // RELLENAR MATRIZ A
    for (int i = 0; i < nFilas; i++) {
      for (int j = 0; j < nColumnas; j++) {
        System.out.println("Matriz[" + i + "] " + "[" + j + "]");
        matrizA[i][j] = entrada.nextInt();
      }
    }

    // RELLENAR MATRIZ B
    for (int i = 0; i < nFilas; i++) {
      for (int j = 0; j < nColumnas; j++) {
        matrizB[j][i] = matrizA[i][j];
      }
    }

    // IMPRIMIR MATRIZ A
    System.out.println("--- Matriz A (original) ---");
    for (int i = 0; i < nFilas; i++) {
      for (int j = 0; j < nColumnas; j++) {
        System.out.print(matrizA[i][j] + " ");
      }
      System.out.println();
    }

    // IMPRIMIR MATRIZ B
    System.out.println("--- Matriz B (traspuesta) ---");
    for (int i = 0; i < nColumnas; i++) {
      for (int j = 0; j < nFilas; j++) {
        System.out.print(matrizB[i][j] + " ");
      }
      System.out.println();
    }

    // MATRIZ CUADRADA
    cuadrada = (nFilas == nColumnas);
    if (cuadrada) {
      System.out.println("La matriz es cuadrada");
    } else {
      System.out.println("La matriz no es cuadrada");
    }

    // ----- Verificación -----
    esTraspuesta = true;
    if (cuadrada) {
      for (int i = 0; i < nFilas; i++) {
        for (int j = 0; j < nColumnas; j++) {
          if (matrizA[i][j] != matrizB[i][j]) {
            esTraspuesta = false;
          }
        }
      }
    } else {
      esTraspuesta = false;
    }

    // RESULTADO
    if (esTraspuesta) {
      System.out.println("La matriz ingresada es igual a su traspuesta (es simetrica)");
    } else {
      System.out.println("La matriz ingresada no es igual a su traspuesta");
    }
  }
  public static void ejercicio_17() {
        int matriz [][] = crearMatrizIdentidad(7);
        imprimir(matriz);
      }

      public static int[][] crearMatrizIdentidad(int tamano) {
        int[][] m = new int[tamano][tamano];

        for (int i = 0; i < tamano; i++) {
          for (int j = 0; j < tamano; j++) {
            if (i == j) {
              m[i][j] = 1;
            } else {
              m[i][j] = 0;
            }
          }
        }
        return m;
      }

      public static void imprimir(int[][] m) {
        for (int[] fila : m) {
          for (int valor : fila) {
            System.out.print(valor + " ");
          }
          System.out.println();
        }
      }
      public static void main(String[] args) {
          ejercicio_17();
      }
}
