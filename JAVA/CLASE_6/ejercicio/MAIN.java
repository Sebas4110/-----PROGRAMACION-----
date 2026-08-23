package ejercicio;

import javax.swing.JOptionPane;

public class MAIN {
  public static void main(String[] args) {
    Movement coords = new Movement(0, 0);
    String mov;
    int cantidad;
    boolean salir = true;
    while (salir) {
      mov = JOptionPane.showInputDialog(
          "dame la direccion a la cual quieres moverte: Arriba(w), Abajo(s), derecha(d), izquierda(a), salir(e)");

      cantidad = Integer.parseInt(JOptionPane.showInputDialog("cuantas casillas quieres moverte?"));

      switch (mov) {
        case "w", "W":
          coords.arriba(cantidad);
          break;
        case "S", "s":
          coords.abajo(cantidad);
          break;
        case "d", "D":
          coords.derecha(cantidad);
          break;
        case "a", "A":
          coords.izquierda(cantidad);
          break;
        case "e", "E":
          salir = false;

      }
      JOptionPane.showMessageDialog(null, "La coords actuales son " + coords.getCoords());
    }
  }
}
