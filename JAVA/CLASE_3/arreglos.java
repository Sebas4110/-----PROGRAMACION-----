package CLASE_3;

public class arreglos {
public static void main(String[] args) {
    int [] numeros = new int[3];
    numeros[0] = 10;
    numeros[1] = 20;
    numeros[2] = 35;

    int[] numeros2 = {23,45,78,89};

    String[] nombre = {"enzo", "felipe", "ciro"};

    System.out.println(nombre[2]);
    System.out.println(nombre[0]);
    System.out.println(numeros2.length);

    //imprimir todos

    for (int i = 0; i < nombre.length; i++){
      System.out.print(nombre[i]+", ");
    }

    //for EACH
    for (String i : nombre) {
      System.out.println("\n---"+i);
  }

  double[] notas = {1.5, 3, 3.1, 4, 3.5, 2.3, 1.5};
  double suma = 0;
  double maximo = notas[0];
  for (double nota : notas) {
    suma += nota;
    if (nota > maximo) {
      maximo = nota;
    }
  }
  double promedio = suma / notas.length;
  System.out.println("el promedio de las notas fue de: "+ promedio);
  System.out.println("y la nota maxima fue de: "+ maximo);

  }
}
