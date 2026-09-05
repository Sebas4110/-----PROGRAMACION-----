public class Animal {
  public void hacerSonido() {
    System.out.println("El animal hace un sonido");
  }
}


class Perro extends Animal {
  @Override
  public void hacerSonido() {
    System.out.println("*ladra*");
  }
}


class Gato extends Animal {
  @Override
  public void hacerSonido() {
    System.out.println("*maulla*");
  }
}


class pruebaAnimal {
  static void imprimirSonido(Animal animal) { // metodo poliformo
    animal.hacerSonido();
  }

  public static void main(String[] args) {
    var animal1 = new Perro();
    var animal2 = new Gato();

    imprimirSonido(animal1);
    imprimirSonido(animal2);

  }
}


/*el polimorfismo significa multiples formas, lo c ual seria diferentes comportamientos
dependiendo del tipo de dato.
esto trabaja con herencia y sobreescritura.
existen tambien clases abstractas y metodos abstractos, los cuales no se pueden instanciar, pero si se pueden heredar.


*/
