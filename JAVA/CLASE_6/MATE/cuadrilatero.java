package MATE;

public class cuadrilatero {
  private float lado1, lado2;
  // primero clases, despues atributos y despues metodos

  //metodos
  public cuadrilatero(float lado1, float lado2){
    this.lado1 = lado1;
    this.lado2 = lado2;

  }

  public cuadrilatero(float lado1) {
    this.lado1 = this.lado2 = lado1;
  }

  public float getPerimetro(){
    float perimetro = 2 *(lado1 +lado2);
    return perimetro;
  }

  public float getArea(){
    var area = lado1 *lado2;
    return area;
  }
}
