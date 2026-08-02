package clase_2;

public class switch {
    public static void main(String[] args) {
        int num1, num2, suma, resta, multi, divi;
        char operacion;
        num1 = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero: "));
        num2 = Integer.parseInt(JOptionPane.showInputDialog("Escriba un segundo numero: "));

        operacion = JOptionPane.showInputDialog("Escriba la primera letra de la operacion que quiera realizar\n"+
        "s para sumar\n"+
        "r para restar\n"+
        "m para multiplicar\n"+
        "d para dividir").charAt(0);

        switch(operacion){
            case 's' :
            case 'S' : suma = num1 + num2;
            JOptionPane.showMessageDialog(null, "La suma de los 2 numeros es: "+ suma);
                break;

            case 'r' :
            case 'R' : resta = num1 - num2;
            JOptionPane.showMessageDialog(null, "La resta de los 2 numeros es: "+ resta);
                break;

            case 'm' :
            case 'M' : mul = num1 * num2;
            JOptionPane.showMessageDialog(null, "La multiplicacion de los 2 numeros es: "+ multi);
                break;

            case 'd' :
            case 'D' : div = num1 / num2;
            JOptionPane.showMessageDialog(null, "La division de los 2 numeros es: "+ divi);
                break;
        }
    }
}