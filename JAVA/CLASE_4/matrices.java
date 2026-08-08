public class matrices {
  public static void main(String[] args) {
    // las matrices son filas y columnas y java lo considera como objeto
    //una fila de 3x5 seria como si fueran 3 arreglos
    //literal son coordenadas
    //la matriz cuadrada es cuando tiene el mismo numero de filas y columnas
    int matriz [][] = {{1,2,3,4,5},{11,12,13,14,15},{21,22,23,24,25}};

    //imprimir matrices

    for (int i = 0; i < 3 ; i++){
      for (int j = 0; j < 5; j++){
        System.out.print(matriz[i][j] + " ");
      }
      System.out.println();
    }

  }
  }


