import java.util.Scanner;
import javax.swing.JOptionPane;

public class e29 {
  public static void main(String[] args) {
    System.out.println("Por:\n - Sebastian Hernandez Muñoz\n - Juan Esteban Ciro Gallego\n");

    Scanner sc = new Scanner(System.in);
    int nFilas, nColumnas, matrizA[][];
    boolean cuadrada;

    // CREAR MATRICES
    nFilas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de filas:"));
    nColumnas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de columnas:"));
    matrizA = new int[nFilas][nColumnas];
    System.out.println("Escriba cada elemento de la matriz despues del enter");

    // RELLENAR MATRIZ
    for (int i = 0; i < nFilas; i++) {
      for (int j = 0; j < nColumnas; j++) {
        System.out.println("Matriz[" + i + "] " + "[" + j + "]");
        matrizA[i][j] = sc.nextInt();
      }
    }

    // VERIFICAR SI LA MATRIZ ES CUADRADA
    cuadrada = (nFilas == nColumnas);
    if (cuadrada) {
      System.out.println("La matriz es cuadrada");
    } else {
      System.out.println("La matriz no es cuadrada");
    }

    sc.close();
  }
}
