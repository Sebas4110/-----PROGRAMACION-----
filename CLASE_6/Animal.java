public class Animal {

  protected void comer() {
    System.out.println("Come mucho");
  }

  protected void dormir() {
    System.out.println("Duerme muchas horas al día");
  }

  static class Perro extends Animal {

    public void ladrar() {
      System.out.println("Puede ladrar");
    }
  }

  static class pruebaAnimal {

    public static void main(String[] args) {
      Animal animal1 = new Animal();

      animal1.comer();

      Perro perro1 = new Perro();
      perro1.comer();
      perro1.dormir();
      perro1.ladrar();

    }

  }

}
