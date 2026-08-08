package CLASE_1;

import java.util.Scanner;

// como pedir algo externo
public class input {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String nombre;

        System.out.println("escriba su nombre: ");

        // nombre = entrada.next();
        // next() es solo para texto y solo imprime la primera la palabra
        nombre = entrada.nextLine();
        // nextLine()para mostrar varias palabras
        System.out.println("hola " + nombre);

        byte edad;
        System.out.println("cuantos años tines?");
        edad = entrada.nextByte();

        System.out.println("tienes " + edad);

        // todo lo escrito en el teclado va a ser string
    }
}
