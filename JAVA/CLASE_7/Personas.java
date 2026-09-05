public class Personas {
  static int contadorPersonas = 0;
  private String nombre;
  private String apellidos;

  public Personas(String nombre, String apellidos) {
    this.nombre = nombre;
    this.apellidos = apellidos;

    // INCREMENTAR EL ATRIBUTO ESTATICO
    Personas.contadorPersonas++;
  }

  @Override
  public String toString() {
    return "Nombre: " + this.nombre + ", Apellidos: " + this.apellidos + " , Dir Men.: "
        + super.toString();
  }

  public String getNombre() {
    return nombre;
  }

  public void setNombre(String nombre) {
    this.nombre = nombre;
  }

  public String getApellidos() {
    return apellidos;
  }

  public void setApellidos(String apellidos) {
    this.apellidos = apellidos;
  }

  public static void main(String[] args) {
    System.out.println("*** Creacion de Clase y Objeto Persona ***");
    System.out.println("*** Variables Static ***");

    var objeto1 = new Personas("Ciro", "Mania");
    System.out.println(objeto1);
    System.out.println("variable estatica "+ Personas.contadorPersonas);

    var objeto2 = new Personas("Santi", "Gomez");
    System.out.println(objeto2);
    System.out.println("variable estatica "+ Personas.contadorPersonas);

  }
}

