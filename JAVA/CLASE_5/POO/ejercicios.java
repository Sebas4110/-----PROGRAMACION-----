package POO;

public class ejercicios {

  public static class Aparatos {
    String nombre, marca, tipo;
    int año;
    //metodos
    public void prende() {
      System.out.println("El " + nombre + " enciende correctamente");
    }

    public void imagenes() {
      System.out.println("El "+ nombre + " puede mostrar imagenes");
    }

    public void internet() {
      System.out.println("El "+ nombre +" puede navegar con internet");
    }
    public void especi(){
      System.out.println("El nombre del aparato es: " + nombre);
      System.out.println("El tipo del aparato es: " + tipo);
      System.out.println("La marca del aparato es: " + marca);
      System.out.println("El año de salida del aparato es: " + año);
    }
  }


  public static void main(String[] args) {
    Aparatos celular = new Aparatos();
    Aparatos laptop = new Aparatos();
    Aparatos TV = new Aparatos();

    celular.nombre = "Samsung Galaxy S26";
    celular.marca = "Samsung";
    celular.tipo = "Celular";
    celular.año = 2025;
    celular.especi();
    celular.prende();
    celular.imagenes();
    celular.prende();

    laptop.nombre = "Asus tuf gaming A15";
    laptop.marca = "Asus";
    laptop.tipo = "portatil";
    laptop.año = 2025;
    laptop.especi();
    laptop.prende();
    laptop.imagenes();
    laptop.prende();



    TV.nombre = "Samsung Neo QLED";
    TV.marca = "Samsung";
    TV.tipo = "TV";
    TV.año = 2024;
    TV.especi();
    TV.prende();
    TV.imagenes();
    TV.prende();



  }
}