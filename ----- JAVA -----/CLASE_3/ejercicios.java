package CLASE_3;

import java.util.Scanner;

public class ejercicios {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int opcion;
        System.out.println("Que ejercicio desea hacer?\n"+
        "1) ejercicio 1\n"+
        "2) ejercicio 2\n"+
        "3) ejercicio 3\n"+
        "4) ejercicio 4\n"+
        "5) ejercicio 5\n");

        opcion = entrada.nextInt();
        switch (opcion) {
            case 1:
                ejercicio_1(entrada);
                break;
            case 2:
                ejercicio_2(entrada);
                break;
            case 3:
                ejercicio_3(entrada);
                break;
            case 4:
                ejercicio_4(entrada);
                break;
            case 5:
                ejercicio_5(entrada);
                break;
            default:
                System.out.println("Numero no valido");
        }

    }



  public static void ejercicio_1(Scanner entrada){

    int num;

    do {
        System.out.println("Ingrese 0 para salir");
        System.out.println("dame un numero y te dire si es positivo o negativo: ");
        num = entrada.nextInt();
        if (num > 0){
          System.out.println("El numero es positivo");
        }
        else if (num == 0){
          System.out.println("el numero es cero");
        }
        else if (num < 0) {
          System.out.println("El numero es negativo");
        }
    } while (num != 0);

    System.out.println("hasta luego");
  }

  public static void ejercicio_2(Scanner entrada) {
    int num;

    do {
      System.out.println("Ingrese 0 para salir");
      System.out.println("dame un numero y te dire si es par o impar: ");
      num = entrada.nextInt();
      if (num %2 == 0 & num != 0) {
        System.out.println("El numero es par");
      } else if (num == 0) {
        System.out.println("el numero es cero");
      } else if (num %2 != 0) {
        System.out.println("El numero es impar");
      }
    } while (num != 0);
    System.out.println("hasta luego");
  }

  public static void ejercicio_3(Scanner entrada) {
    int i = 0, num;

    do {
      System.out.println("dame numeros (para parar, digite un numero negativo) ");
      num = entrada.nextInt();
      if (num > 0) {
        i++;
      } ;
    } while (num > 0);
    System.out.println("CERRANDO...");
    System.out.println("el total de numeros introducidos fueron " + i);
  }

  public static void ejercicio_4(Scanner entrada) {
    int i = 0;
    int elec;
    int num = (byte) (Math.random() * (100 - 1 + 1)) + 1;
    System.out.println("===== adivina el numero del 1 al 100 =====");
    do{
      System.out.println("dime un numero: ");
      elec = entrada.nextInt();
      if (elec != num) {
        i++;
        System.out.println("intentelo otra vez");
      }
    }while (elec != num);
    i++;
    System.out.println("¡¡ lograste encontrar el numero !!; numero de intentos: "+ i);

  }

  public static void ejercicio_5(Scanner entrada) {
    int num, num2 = 0;

    System.out.println("presione 0 para terminar");
    do{
      System.out.println("ingresa un numero para sumar");
      num = entrada.nextInt();
      num2 += num;

    }while (num != 0);
    System.out.println("la suma total fue de "+ num2 );
  }
}