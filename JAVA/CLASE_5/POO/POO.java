// package POO;

public class POO {
  public static class Carro {
    // atributos
    String color, marca;
    int km;

  }

  public static void main(String[] args) {
    Carro carro1 = new Carro();
    carro1.color = "Amarillo";
    carro1.marca = "Ferrari";
    carro1.km = 0;
    System.out.println("La marca del carro 1 es: " + carro1.marca);
    System.out.println("El color del carro 1 es: " + carro1.color);
    System.out.println("El kilometraje del carro 1 es: " + carro1.km);

    Carro carro2 = new Carro();
    carro2.color = "azul";
    carro2.marca = "BMW";
    carro2.km = 0;
  }

}
