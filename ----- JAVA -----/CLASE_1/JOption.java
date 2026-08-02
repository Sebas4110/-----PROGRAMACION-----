package CLASE_1;

import javax.swing.JOptionPane;

public class JOption {
    public static void main(String[] args) {
        String cadena;
        int entero;
        char letra;
        // la variable char es una letra
        double decimal;

        cadena = JOptionPane.showInputDialog("Escriba una frase");
        entero = Integer.parseInt(JOptionPane.showInputDialog("escriba un numero entero"));
        letra = JOptionPane.showInputDialog("Escriba una letra").charAt(0);
        decimal = Double.parseDouble(JOptionPane.showInputDialog("Escriba un numero decimal"));

        JOptionPane.showMessageDialog(null, "la cadena que escribio fue: "+ cadena);
        JOptionPane.showMessageDialog(null, "el numero que escribio fue: "+ entero);
    }
}