package CLASE_1;


public class Prueba {

    public static void main(String[] args) {
        System.out.println("Hola, mundo!");
        System.out.println("UPB Marinilla");
        System.out.println("Sebastián Hernández");

        // comentar en bloque

        //escribir variable
        byte dato1;
        dato1 = 15;
        // solo se crea la variable, no se le asigna un valor todavia

        short dato2 = 243;
        // en esta ya se crea la variable y se le asigna un valor

        System.out.println(dato2);

        //sout más tabulador = system.outprintLn()
        // linea amarilla significa que no se ha utilizado todavia el nombre de la variable
        // solo puede existir un main
        byte edad = 15;
        System.out.println("Mi nombre es Sebastián y tengo" + edad);


        //tipo de datos flotantes
        float pi = 3.141516f;
        String nombre = "Sebastián";

        //constante: no se puede cambiar valores
        final int edad2 = 16;
    }
}
