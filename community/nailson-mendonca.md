## Satisfação a todos me chamo Nailson Mendonça, sou professor de Matemática e pretendo entender o uso da tecnologia para facilitar o ensino da mesma.




## proponho esse projeto.
# Projeto: Calculadora de Área de Triângulo

## Descrição
Este projeto implementa uma calculadora de área de triângulo em Python, demonstrando boas práticas de programação e documentação.

## Estrutura do Código

### 1. Classe Principal `TriangleCalculator`

```python
class TriangleCalculator:
    """
    Classe para cálculos relacionados a triângulos.
    """
    
    @staticmethod
    def validate_input(value: float, name: str) -> bool:
        """
        Valida se o valor de entrada é positivo.
        """
        if value <= 0:
            print(f"Erro: {name} deve ser um valor positivo!")
            return False
        return True

    @staticmethod
    def calculate_area(base: float, height: float) -> float:
        """
        Calcula a área do triângulo.
        """
        return (base * height) / 2
```

### 2. Função Principal `main()`

```python
def main():
    calculator = TriangleCalculator()
    
    while True:
        print("\n=== Calculadora de Área do Triângulo ===")
        try:
            base = float(input("Digite o valor da base do triângulo: "))
            altura = float(input("Digite o valor da altura do triângulo: "))
            
            if not all([
                calculator.validate_input(base, "Base"),
                calculator.validate_input(altura, "Altura")
            ]):
                continue
            
            area = calculator.calculate_area(base, altura)
            print(f"\nA área do triângulo é: {area:.2f} unidades quadradas")
            
        except ValueError:
            print("Erro: Por favor, digite apenas números!")
            continue
            
        continuar = input("\nDeseja calcular outro triângulo? (s/n): ").lower()
        if continuar != 's':
            print("\nObrigado por usar a calculadora de triângulos!")
            break

if __name__ == "__main__":
    main()
```

## Funcionalidades Implementadas

1. **Validação de Entrada**
   - Verifica se os valores são positivos
   - Trata erros de digitação (valores não numéricos)

2. **Cálculo de Área**
   - Utiliza a fórmula: `área = (base * altura) / 2`
   - Retorna resultado com 2 casas decimais

3. **Interface Amigável**
   - Menu interativo
   - Mensagens claras de erro
   - Opção de calcular múltiplos triângulos

## Como Executar

1. Salve o código em um arquivo `triangle_calculator.py`
2. Execute no terminal:
   ```bash
   python triangle_calculator.py
   ```

## Exemplo de Uso

```plaintext
=== Calculadora de Área do Triângulo ===
Digite o valor da base do triângulo: 5
Digite o valor da altura do triângulo: 3

A área do triângulo é: 7.50 unidades quadradas

Deseja calcular outro triângulo? (s/n): n

Obrigado por usar a calculadora de triângulos!
```

## Tratamento de Erros

1. **Entrada Inválida**
   ```plaintext
   Digite o valor da base do triângulo: abc
   Erro: Por favor, digite apenas números!
   ```

2. **Valores Negativos**
   ```plaintext
   Digite o valor da base do triângulo: -5
   Erro: Base deve ser um valor positivo!
   ```

## Melhorias Futuras

1. Adicionar cálculos usando diferentes fórmulas:
   - Três lados (Fórmula de Heron)
   - Dois lados e um ângulo
   - Coordenadas dos vértices

2. Implementar interface gráfica

3. Adicionar testes unitários

4. Suporte a diferentes unidades de medida

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Faça commit das alterações
4. Push para a branch
5. Crie um Pull Request

## Licença

Este projeto está sob a licença MIT.
