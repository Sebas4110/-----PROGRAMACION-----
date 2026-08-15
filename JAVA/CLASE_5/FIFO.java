
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class FIFO {
  public static void main(String[] args) {
      /*Queue<String> fila = new LinkedList<>();
      fila.offer("Juan Jose");
      fila.offer("Ciro");
      fila.offer("sebastian");
      fila.offer("  Bryan");

      System.out.println(fila);

      //usar el primer dato
      System.out.println("\nPersona atendida");
      String atendido =fila.poll();

      System.out.println("primera persona atendida: " + atendido);
      System.out.println("\nPersona pendientes por ser atendida");
      System.out.println(fila);
    */
    ejercicio_2();
  }
public static void ejercicio_1() {
  Stack<String> pagina = new Stack<>();
  pagina.push("Goggle");
  pagina.push("Youtube");
  pagina.push("Wikipedia");
  pagina.push("Git hub");

  System.out.println(pagina);

  String pgEliminada = pagina.pop();

  System.out.println("\nLa paigna eliminada fue: "+ pgEliminada);
  System.out.println("\nEl historial es: "+ pagina);
  }
  public static void ejercicio_2() {
    Queue<String> impresion = new LinkedList<>();
    impresion.offer("TareaJava");
    impresion.offer("Informe");
    impresion.offer("Factura");
    impresion.offer("HojaVida");

    System.out.println(impresion);
    String first = impresion.peek();
    System.out.println("\nSe va a imprimir la siguiente pagina: "+ first);

    String impre = impresion.poll();
    System.out.println("\nLa cola restante es: "+impresion);

  }
}
