package ejercicio;

public class Movement {
  private int x = 0;
  private int y = 0;

  public Movement(int x, int y) {
    this.x = x;
    this.y = y;
  }

  public String getCoords() {
    return "(" + this.x + ", " + this.y + ")";
  }


  public void derecha(int cantidad) {
    this.x += cantidad;
  }

  public void izquierda(int cantidad) {
    this.x -= cantidad;
  }

  public void arriba(int cantidad) {
    this.y += cantidad;
  }

  public void abajo(int cantidad) {
    this.y -= cantidad;
  }


}
