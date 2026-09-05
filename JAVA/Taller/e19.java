import javax.swing.JOptionPane;

public class e19 {
  public static void main(String[] args) {
    int i = 0;
    final byte NUM = (byte) ((Math.random() * (100 - 1 + 1)) + 1);
    byte intento;

    int confirmacion = JOptionPane.showConfirmDialog(null,
        "Juguemos un jueguito, yo pensaré en un número random entre el 1 y 100 y vos deberás adivinar cual es. ¿Te animas?",
        "Juego de Adivinanza", JOptionPane.YES_NO_OPTION);

    if (confirmacion != JOptionPane.YES_OPTION) {
      return;
    }

    do {
      intento = Byte.parseByte(JOptionPane.showInputDialog("Adivina el número (1-100):"));
      i++;

      if (intento < NUM) {
        JOptionPane.showMessageDialog(null, "Más arriba");
      } else if (intento > NUM) {
        JOptionPane.showMessageDialog(null, "Más abajo");
      }

    } while (intento != NUM);

    JOptionPane.showMessageDialog(null,
        "¡Ese es! El número era " + NUM + ". Solo te tomo: " + i + " intentos");

    System.out.println("FIN");
  }
}
