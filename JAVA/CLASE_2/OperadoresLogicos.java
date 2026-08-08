package CLASE_2;


import java.util.Scanner;
import javax.swing.JOptionPane;

public class OperadoresLogicos {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int a,b;
        a = 25;
        b = 78;

        boolean resultado = a > b;
        System.out.println(resultado);

        resultado = a < b;
        System.out.println(resultado);

        resultado = a < b-53;
        System.out.println(resultado);

        resultado = a <= b-53;
        System.out.println(resultado);

        resultado = a == b-53;
        System.out.println(resultado);

        String nombre1 = "ranger";
        String nombre2 = "ranger";

        System.out.println(nombre1 == nombre2);

        int num6;
        String mensaje;
        num6 = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero"));
        mensaje = (num6 % 2 == 0)? "El numero es par" : "El numero es impar";

        JOptionPane.showMessageDialog(null,mensaje);

        int num1, dato = 8;

        num1 = Integer.parseInt(JOptionPane.showInputDialog("Escriba que un numero del 1 al 10: "));

        if (num1 == dato){
            JOptionPane.showMessageDialog(null, "Adivino el numero");
        }
        else{
            JOptionPane.showMessageDialog(null, "No adivino el numero");
        }
    }
}