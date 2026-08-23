package ejercicio_2;

public class sucursal {
  private int numSucursal;
  private String direccion;
  private String ciudad;

  public sucursal(int numSucursal, String direccion, String ciudad) {
    this.numSucursal = numSucursal;
    this.direccion = direccion;
    this.ciudad = ciudad;
  }

  public int getNumSucursal() {
    return numSucursal;
  }

  public String getDireccion() {
    return direccion;
  }

  public String getCiudad() {
    return ciudad;
  }
}
