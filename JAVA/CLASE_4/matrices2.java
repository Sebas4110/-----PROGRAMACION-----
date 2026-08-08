
import java.util.Scanner;
import javax.swing.JOptionPane;

public class matrices2 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    int nFila, nColumna, matriz2[][];
    nFila = Integer.parseInt(JOptionPane.showInputDialog("ingrese el numero de filas"));
    nColumna = Integer.parseInt(JOptionPane.showInputDialog("ingrese el numero de columnas"));

    matriz2 = new int[nFila][nColumna];
    System.out.println("Escriba cada elemento de la matriz despues del enter");

    for (int i = 0 ; i < nFila; i++) {
      for (int j = 0 ; j < nColumna; j++){
        System.out.println(matriz2[i][j] + "");
      }
      System.out.println("");
    }

    if (nFila == nColumna) {
      System.out.println("\nla matriz es cuadrada");
    }else {
      System.out.println("\nla matriz no es cuadrada");
    }
  }
}
