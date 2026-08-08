package PROYECTO_C2;

import java.util.Scanner;

public class calculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("===== BIENVENIDO =====");
        System.out.println("¿Qué desea hacer?\n"+
        "1) Suma\n"+
        "2) Resta\n"+
        "3) Multiplicación\n"+
        "4) División");
        Byte op = sc.nextByte();
        switch (op) {
            case 1:
                suma();
                break;
            default:
                System.out.println("Numero incorrecto o nulo");
                System.out.println("Intentelo nuevamente");
        }

    }
    public static void suma() {
        System.out.print("===== SUMA =====");

    }
}
