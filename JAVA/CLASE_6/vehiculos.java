

public class vehiculos {
  protected void marca(){
    System.out.println("mi marca es: ");
  }
  protected void modelo(){
    System.out.println("es modelo: ");
  }
  protected void color(){
    System.out.println("soy de color: ");
  }
}
  class transportePublico extends vehiculos{

    public void capacidad(){
      System.out.println("puedo transportar");
    }

  }

  class prueba {
    public static void main(String[] args) {
      vehiculos vehiculo1 = new vehiculos();
      vehiculo1.marca();

      transportePublico taxi = new transportePublico();
      taxi.capacidad();
    }
  }

