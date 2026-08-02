package CLASE_2;


import java.util.Scanner;

public class operadores {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        // el escaner
        int num1, num2, suma, resta, multi, div, restos;
        int op;

        System.out.println("escriba dos numeros: ");
        num1 = entrada.nextInt();
        num2 = entrada.nextInt();

        suma = num1 + num2;
        //operadores aritmeticos con asignación
        restos = num1 % num2;
        resta = num1 - num2;
        multi = num1 * num2;
        div = num1 / num2;

        System.out.println("que quiere hacer?");
        System.out.println("1)suma");
        System.out.println("2)resta");
        System.out.println("3)multiplicación");
        System.out.println("4)división");

        op = entrada.nextByte();
        //leccion de vida: por cualquier letra, java jode, aunque este bien la letra, si no esta en mayuscula o minuscula, jode.
        //y existe un next para todo

        switch (op) {//Ha vuelto el Dius Match, y esta mejorado!

        case 1:
            System.out.println("la suma de "+ num1 + " con "+ num2 + " da como resultado " + suma);
            break;
        case 2:
            System.out.println("la resta de "+ num1 + " con "+ num2 +" da un resultado de: "+ resta);
            break;
        case 3:
            System.out.println("la multiplicación de "+ num1 + " con "+ num2 +" da un resultado de: "+ multi);
            break;
        case 4:
            System.out.println("la división de "+ num1 + " con "+ num2 +" da un resultado de: "+ div);
            break;
        default:
            System.out.println("intente con otro numero");
        };

        // OPERADORES DE INCREMENTO Y DECREMENTO

        int numero3 = 11;
        System.out.println(numero3);

        numero3 += 5;
        System.out.println(numero3);

        numero3 ++ ;//incremento de uno en uno
        System.out.println(numero3);

        numero3 -- ;//decremento de uno en uno
        System.out.println(numero3);
        // control + D sirve para editar mismas palabras, de arriba hacia abajo

        int x = 12, y;
        y = ++x;//aqui suma y después imprime
        System.out.println(y);

        y = x++;//aqui imprime y despues suma
        System.out.println(y);


        //EJERCICIO con el decremento

        int z = 5, a;

        a = --z;
        System.out.println("en valor de z es "+z);
        System.out.println("el valor de a es "+ a);

        a = z--;

        System.out.println("en valor de z es "+z);
        System.out.println("el valor de a es "+ a);
    }

}
