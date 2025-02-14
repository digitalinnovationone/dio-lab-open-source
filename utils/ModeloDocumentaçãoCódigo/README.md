# Projeto Exemplo
<!--Aqui você pode colocar o título do seu projeto-->

## 📋 Descrição  do projeto
<!--Aqui você pode descrever as condições que seu código deverá atender e o resultado esperado ao executar-->
O projeto tem como finalidade fornecer as informações do holerite de um funcionário a partir da quantidade de horas trabalhadas e o valor da sua hora. Existem algumas considerações a serem realizadas no cálculo, como: INSS, FGTS e IR (Descontos). O projeto será todo desenvolvido em C, utilizará uma boa fundamentação de funções para conseguir realizar os calculos e atender à regra de negócio do projeto.

Imposto de Renda (IR) e FGTS com base nas regras abaixo:
* O INSS corresponde a 10% do Salário Bruto.
* O FGTS corresponde a 11% do Salário Bruto.
* IR depende do valor salário bruto (conforme tabela abaixo):
    - Salário Bruto até 1000 (inclusive) - isento.
    -   Salário Bruto acima de 1000 desconto de 10%.
* Para calcular o Salário Líquido você deve subtrair o Salário Bruto dos descontos. Vale
ressaltar que o FGTS não é descontado para o cálculo do salário líquido.

## Exemplo de Entrada e Saída:
<!--Demonstração de uma entrada e a saída referente à entrada-->
Veja um exemplo de saída considerando as entradas:
* `Hora:` 15
* `Quantidade de Horas Trabalhadas:` 100
<!--Entrada-->

```
Salário Bruto: (15 * 100) --> R$ 1500,00
(-) IR (10%)              --> R$ 150,00
(-) INSS ( 10%)           --> R$ 150,00
FGTS (11%)                --> R$ 165,00
Total de descontos        --> R$ 300,00
Salário Liquido           --> R$ 1200,00
```
<!--Saida-->
### Código:
<!--Demonstração de cada trecho do código e explicação da função de cada função-->
>Trechos referentes ao código [exemplo.c](https://github.com/RyanBrittes/dio-lab-open-source/blob/main/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c)

* Importação de bibliotecas e declaração da função responsável pelo Cálculo do Salário:
https://github.com/RyanBrittes/dio-lab-open-source/blob/9814a75afdf715f38b31b91f6d6212a6b8900184/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c#L1-L7

* Função responsável pelo cálculo do IR
https://github.com/RyanBrittes/dio-lab-open-source/blob/9814a75afdf715f38b31b91f6d6212a6b8900184/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c#L9-L13

* Função responsável pelo cálculo do INSS 
https://github.com/RyanBrittes/dio-lab-open-source/blob/9814a75afdf715f38b31b91f6d6212a6b8900184/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c#L15-L19

* Função responsável pelo cálculo do FGTS 
https://github.com/RyanBrittes/dio-lab-open-source/blob/9814a75afdf715f38b31b91f6d6212a6b8900184/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c#L21-L25

* Função responsável pela chamada de outras funções e ordenação dos calculos para imprimir ao usuário o resultado dos valores
https://github.com/RyanBrittes/dio-lab-open-source/blob/9814a75afdf715f38b31b91f6d6212a6b8900184/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c#L27-L57

* Função principal, sendo responsável por inicializar a lógica de funcionamento do código e chamada das funções.
https://github.com/RyanBrittes/dio-lab-open-source/blob/9814a75afdf715f38b31b91f6d6212a6b8900184/utils/ModeloDocumenta%C3%A7%C3%A3oC%C3%B3digo/exemplo.c#L59-L65


### ✒️ Autor

👨‍💻 Nome do autor <br>
📕 Ocupação do autor
<!--Neste trecho podem ser inseridas informações do autor do projeto do projeto-->

### Adicional:
Os trechos de código foram utilizados utilizando apenas o MarkDown, para saber como utilizar este recurso acesso o [GUIA DO GITHUB](https://docs.github.com/pt/get-started/writing-on-github/working-with-advanced-formatting/creating-a-permanent-link-to-a-code-snippet)
