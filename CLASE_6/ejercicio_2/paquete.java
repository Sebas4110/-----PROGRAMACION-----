package ejercicio_2;

public class paquete {
  private String numReferencia;
  private String dni;
  private double peso;
  private String priori; // "normal", "alta", "express"
  private sucursal sucursal;

  private static final double Precio_Kilo = 1000;
  private static final double priori_Alta = 10000;
  private static final double Express = 20000;

  public paquete(String numReferencia, String dni, double peso, String priori, sucursal sucursal) {
    this.numReferencia = numReferencia;
    this.dni = dni;
    this.peso = peso;
    this.priori = priori;
    this.sucursal = sucursal;
  }

  public String getnumReferencia() {
    return numReferencia;
  }

  public String getdni() {
    return dni;
  }

  public double getpeso() {
    return peso;
  }

  public String getpriori() {
    return priori;
  }

  public sucursal getSucursal() {
    return sucursal;
  }

  public double calcularPrecio() {
    double precio = peso * Precio_Kilo;

    if (priori.equalsIgnoreCase("alta")) {
      precio += priori_Alta;
    } else if (priori.equalsIgnoreCase("express")) {
      precio += Express;
    }

    return precio;
  }


}
