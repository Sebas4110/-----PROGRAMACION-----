package CLASE_3;

import java.util.Scanner;

public class bucles {
    public static void main(String[] args) {
        // bucle while
        int i = 1;

        while (i <= 10) {

            System.out.println(i);
            i++;
        }
        Scanner entrada = new Scanner(System.in);
        String passwords;
        //bucle Do while
        do {
            System.out.println("ingrese su contraseña");
            passwords = entrada.nextLine();
            if (!passwords.equals("hola")){
                System.out.println("Contraseña incorrecta");
            }
        } while (!passwords.equals("hola"));
        System.out.println("Bienvenido al sistema");
        // la '!' significa 'si es diferente a...'

    }
}
