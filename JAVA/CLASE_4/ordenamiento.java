import java.util.Scanner;
import javax.swing.JOptionPane;

public class ordenamiento {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int arreglo[], nElementos;

    nElementos = Integer.parseInt(JOptionPane.showInputDialog("escriba la cantidad de elementos"));
    arreglo = new int[nElementos];
    for (int i = 0; i < nElementos; i++) {
      System.out.println((i + 1) + ". Escriba un numero");
      arreglo[i] = entrada.nextInt();
    }
    for (int i = 0; i < arreglo.length; i++) {
      for (int d = 0; d < (arreglo.length - 1 - i); i++) {
        if (arreglo[d] > arreglo[d + 1]) {
          int aux = arreglo[d];
          arreglo[d] = arreglo[d + 1];
          arreglo[d + 1] = aux;
        }
        System.out.println("ARREGLO ORGANIZADO");


      }
    }
  }
}
