## Ola , eu sou Antonio Helton Vilela (helton1602).
Trabalho como técnico em atomação bancarioa e tenho 13 anos de esperiêscia na área.
tenho 40 anos e estou buscando novas oportunidades.
Formado de analise e desenvolvimento de sistemas, técico em eletrotécinica e automação.

### Vou deixar um projeto em java calculadora simples que dois números e uma operação (+, -, *, /) do usuário.
### Em seguida, ele realiza a operação e exibe o resultado.

import java.util.Scanner;

public class Calculator {

   public static void main(String[] args) {
   
      Scanner scanner = new Scanner(System.in);
      
      System.out.print("Digite o primeiro número: ");
      
      double num1 = scanner.nextDouble();
      
      System.out.print("Digite o segundo número: ");
      
      double num2 = scanner.nextDouble();
      
      System.out.print("Digite a operação (+, -, *, /): ");
      
      char operator = scanner.next().charAt(0);
      
      scanner.close();
      
      double result;

      switch(operator) {
         case '+':
            result = num1 + num2;
            break;
         case '-':
            result = num1 - num2;
            break;
         case '*':
            result = num1 * num2;
            break;
         case '/':
            result = num1 / num2;
            break;
         default:
            System.out.println("Operação inválida.");
            return;
      }

      System.out.println(num1+" "+operator+" "+num2+": "+result);
   }
}
