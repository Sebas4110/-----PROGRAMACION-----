package ejercicio_2;

public class MAIN {
  public static void main(String[] args) {
    sucursal sucursal1 = new sucursal(1, "calle 40e # 84-56", "Medellín");
    sucursal sucursal2 = new sucursal(2, "calle 40e # 84-56", "Rionegro");

    paquete p1 = new paquete("ref # 1", "1234567890", 7.0, "express", sucursal1);
    paquete p2 = new paquete("ref # 1", "0987654321", 8.5, "alta", sucursal1);
    paquete p3 = new paquete("ref # 1", "1122334455", 6.0, "normal", sucursal2);

    System.out.println(p1.getnumReferencia() + " : Precio: " + p1.calcularPrecio());
    System.out.println(p2.getnumReferencia() + " : Precio: " + p2.calcularPrecio());
    System.out.println(p3.getnumReferencia() + " : Precio: " + p3.calcularPrecio());
  }
}
