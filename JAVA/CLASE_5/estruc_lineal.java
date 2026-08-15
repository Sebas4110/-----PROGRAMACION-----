// package CLASE_5;


import java.util.Stack;

public class estruc_lineal {

  /*
   * ===== ESTRUCTURAS LINEALES ===== pilas (stacks) para historiales y memoria colas (queues) para
   * turnos y procesos ===== PILAS ===== se aplica el metodo LIFO (Last In; First Out)
   *
   * push(10) = Insertar pop() = Retirar peek() = Consultar ===== COLAS ===== se aplica el metodo
   * FIFO (First In; First Out)
   *
   * offer(10) = Insertar poll() = Retirar peek() = Consultar
   */
  public static void main(String[] args) {

    Stack<String> platos = new Stack<>();
    platos.push("PLATO1");
    platos.push("PLATO2");
    platos.push("PLATO3");
    platos.push("PLATO4");
    platos.push("PLATO5");

    System.out.println("Pila de platos");
    System.out.println(platos);


    Stack<String> libros = new Stack<>();
    libros.push("Odisea");
    libros.push("Spiderman");
    libros.push("pawpatrol");
    libros.push("Formula 1");
    libros.push("Minions");

    String datoRetirado = libros.pop();
    System.out.println(" \ndato retirado es: "+ datoRetirado);

    System.out.println("\nnuevo listado");
    System.out.println(libros);

    System.out.println("ultimno lanzamiento");
    System.out.println(libros.peek());

  }
}
