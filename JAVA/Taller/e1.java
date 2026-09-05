package Taller;

import javax.swing.JOptionPane;

public class e1 {
  public static void main(String[] args) {
    float nota1, nota2, nota3, promedio;

    System.out.println("Juan Esteban Ciro");
    System.out.println("Sebastián Hernandez");
    nota1 = Float.parseFloat(JOptionPane.showInputDialog("Escribe tu primera nota: "));
    nota2 = Float.parseFloat(JOptionPane.showInputDialog("Escribe tu segunda nota: "));
    nota3 = Float.parseFloat(JOptionPane.showInputDialog("Escribe tu tercera nota: "));

    promedio = (nota1 + nota2 + nota3) / 3;

    JOptionPane.showMessageDialog(null, "tu promedio es de: " + promedio);


  }

}
