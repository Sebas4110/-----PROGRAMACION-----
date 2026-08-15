package POO;

import javax.swing.JOptionPane;

public class metodos {
  public static class Operaciones{
    //atributos
    int suma, resta, multi, divi, num1, num2;

    //Metodos
    public void leerNumer(){
      num1 = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero entero"));
      num2 = Integer.parseInt(JOptionPane.showInputDialog("Escriba otro numero entero"));
    }
    public void sumar(){
      suma = num1 + num2;

    }
    public void mostrarResultado(){
      System.out.println("El resultado de "+ num1 + " + "+ num2 +" es igual a "+ suma);
      System.out.println("El resultado de "+ num1 + " - "+ num2 +" es igual a "+ resta);
      System.out.println("El resultado de "+ num1 + " por "+ num2 +" es igual a "+ multi);
      System.out.println("El resultado de "+ num1 + " dividido por "+ num2 +" es igual a "+ divi);
    }
    public void restar(){
      resta = num1 - num2;
    }
    public void multiplicar(){
      multi = num1 * num2;
    }
    public void dividir(){
      divi = num1 / num2;
    }
    public static void main(String[] args) {
      Operaciones op = new Operaciones();
      op.leerNumer();
      op.sumar();
      op.restar();
      op.multiplicar();
      op.dividir();
      op.mostrarResultado();

    }
  }

}