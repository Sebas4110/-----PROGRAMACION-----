package CLASE_2;


public class clase_math {
    public static void main(String[] args) {

        //raiz cuadrada
        double raiz =    Math.sqrt(99);
        System.out.println(raiz);

        //potencia
        double base = 3, exponente = 3, resultado;
        resultado = Math.pow(base, exponente);
        System.out.println(resultado);

        //redondeo
        // Math.round(numero,decimas)
        final double pi = 3.141592;
        double redondeado = Math.round(pi);

        System.out.printf("el redondeo de %f es %.2f",pi, redondeado);
        //printf significa que se realizara una interpolacion

    }
}
