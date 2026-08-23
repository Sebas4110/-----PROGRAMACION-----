package CLASE_6;

public class Persona {
  // debe tener el mismo nombre de la clase
  // metodo constructor
  String nombre;
  int edad;
  float estatura;
  int documento;

  public Persona(String nombre, int edad, float estatura, int documento) {
    this.nombre = nombre;
    this.edad = edad;
    this.estatura = estatura;
    this.documento = documento;
  }

  public void MostrarDatos() {
    System.out.println("tu nombre es " + nombre);
    System.out.println("tienes " + edad + " años");
    System.out.println("mides "+ estatura + "cm");
    System.out.println("tu documento es: "+ documento);
  }

  public static void main(String[] args) {
    Persona p1 = new Persona("Sebas", 15, 1.68f, 1043309335);
    p1.MostrarDatos();
  }
}
//para mas practicidad, se da clic derecho, accion de codigo fuente, "generate constructors"
//PD: para que funcione, tiene que ser los metodos diferentes(ejm: en el primero, va primero edad y despues nombre;
//en el segundo [con constructor] va primero con nombre y despues edad ).
//NO SE PUEDE TENER DOS METODOS EXACTAMENTE IGUALES
