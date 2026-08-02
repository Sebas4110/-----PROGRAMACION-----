package CLASE_2;

import java.util.Scanner;

public class actividad {
    public static void ejercicio_1() {
        Scanner entrada = new Scanner(System.in);

        float num1, num2, num3;
        System.out.println("dame tres notas y las sumaré");
        System.out.print("Nota 1: ");
        num1 = entrada.nextFloat();
        System.out.print("Nota 2: ");
        num2 = entrada.nextFloat();
        System.out.print("Nota 3: ");
        num3 = entrada.nextFloat();

        float resultado = num1 + num2 + num3;

        System.out.println("la suma daria igual a "+ resultado);
    }

    public static void ejercicio_2(){
        Scanner entrada = new Scanner(System.in);

        float horas, salario;
        System.out.println("dime tus horas trabajadas: ");
        System.out.print("Horas trabajadas: ");
        horas = entrada.nextFloat();

        System.out.println("dime tu salario por hora:");
        System.out.print("Salario por hora: ");
        salario = entrada.nextFloat();

        float total = salario * horas;

        System.out.println("tu salario semanal es de "+ total);

    }
    public static void ejercicio_3() {
        Scanner entrada = new Scanner(System.in);

        float plata;
        System.out.println("Cuanta plata tiene Guillermo?");
        plata = entrada.nextFloat();

        float Luis = plata / 2;
        float Juan = (plata + Luis) / 2;
        System.out.println("En ese caso, Luis tiene $"+ Luis + " y Juan tiene $"+Juan);
    }

    public static void ejercicio_4() {
        Scanner entrada = new Scanner(System.in);

        int costo, cantidad;
        int comisión = 150;
        System.out.println("cuantos carros vendio en el mes?");
        cantidad = entrada.nextInt();
        System.out.println("de que valor eran los carros?");
        costo = entrada.nextInt();

        float comision = comisión * cantidad;
        float porcen = costo * 0.05f;

        float ganancia = 1000 + porcen + comision;
        System.out.println("la ganancia de este mes fue de $"+ ganancia);
    }
    public static void ejercicio_5() {
        Scanner entrada = new Scanner(System.in);

        float nota1, nota2, nota3, nota4;
        System.out.println("dime tus 4 notas del semestre para promediar");
        System.out.print("participación: ");
        nota1 = entrada.nextFloat();
        System.out.print("primer examen parcial: ");
        nota2 = entrada.nextFloat();
        System.out.print("segundo examen parcial: ");
        nota3 = entrada.nextFloat();
        System.out.print("examen final: ");
        nota4 = entrada.nextFloat();

        float promedio = (nota1 * 0.10f) + (nota2 * 0.25f) + (nota3 * 0.25f) + (nota4 * 0.40f);
        System.out.println("tu promedio del semestre fue de " + promedio);
    }
    public static void ejercicio_6() {
        Scanner entrada = new Scanner(System.in);

        double num1, num2, poten1, poten2, expo = 2, resultado;
        System.out.println("dame dos numeros para resolver el cuadrado de la suma (a+b)^2");
        num1 = entrada.nextDouble();
        num2 = entrada.nextDouble();

        poten1 = Math.pow(num1, expo);
        poten2 = Math.pow(num2, expo);
        resultado = (poten1) + 2*(num1 + num2) + (poten2);

        System.out.println("el resultado es "+ resultado);
    }
    public static void ejercicio_7() {
        Scanner entrada = new Scanner(System.in);
        int horas;
        System.out.println("dame un numero de horas y lo convertire en dias, semanas y horas sobrantes");
        horas = entrada.nextInt();
        int semanas, dias, horas2;
        semanas = horas / 168;
        dias = (horas % 168) / 24;
        horas2 = (horas % 168) % 24;
        System.out.println("la comversión seria igual a: "+ semanas+" semanas, "+ dias +" dias y "+ horas2 + " horas");

    }
    public static void ejercicio_8() {
        Scanner entrada = new Scanner(System.in);

        double a, b, c, x1, x2, raiz;

        System.out.println("ingrese los coeficientes de esta ecuación de segundo grado ( ax^2 + bx^2 + c = 0)");
        System.out.println("A: ");
        a = entrada.nextDouble();
        System.out.println("B: ");
        b = entrada.nextDouble();
        System.out.println("C: ");
        c = entrada.nextDouble();

        x1 = (-b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
        x2 = (-b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);

        System.out.println("los posibles resultados con esos numeros son: x1 = "+ x1 + " y x2 = "+ x2);
    }
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //===========  MENÚ ==========
        int opcion;
        System.out.println("Que ejercicio desea hacer?\n"+
        "1) Calificaciones #1\n"+
        "2) Salario semanal\n"+
        "3) Plata\n"+
        "4) Ventas de carros\n"+
        "5) Calificaciones #2\n"+
        "6) calculo matematico\n"+
        "7) Horas, dias y semanas\n"+
        "8) Ecuación");

        opcion = entrada.nextInt();
        switch (opcion) {
            case 1:
                ejercicio_1();
                break;
            case 2:
                ejercicio_2();
                break;
            case 3:
                ejercicio_3();
                break;
            case 4:
                ejercicio_4();
                break;
            case 5:
                ejercicio_5();
                break;
            case 6:
                ejercicio_6();
                break;
            case 7:
                ejercicio_7();
                break;
            case 8:
                ejercicio_8();
                break;
            default:
                System.out.println("Numero no valido");
        }

    }
}
