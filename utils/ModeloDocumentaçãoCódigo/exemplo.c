#include <stdio.h>
#include <locale.h>

//Função calcSalario - utilizada para realizar o calculo do salario bruto
float calcSalario (float n1, float n2){
	return n1 * n2;
}

//Função calcIR - utilizada para realizar o calculo do Imposto de Renda
float calcIR (float n1){
	return n1 > 1000 ? (n1 * 0.1) : (n1 = 0);
	//Função com operador ternário, utilizado no lugar do if, ao fazer a comparação retornará com 10% do valor comparado ou 0
}

//Função calcINSS - utilizada para realizar o calculo do INSS
float calcINSS (float n1){
	return n1 * 0.1;
	//Operação matemática para se obter 10% de um valor
}

//Função calcFGTS - utilizada para realizar o calculo do FGTS
float calcFGTS (float n1){
	return n1 * 0.11;
	//Operação matemática para se obter 11% de um valor
}

//Função vlrHolerite - utilizada para realizar o calculo do salario e impressão dos resultados
float vlrHolerite() {
	setlocale(LC_ALL, "");
	
	float vlrHora;
	float quantHTrabalhada;	
	
	printf("Digite o valor da hora trabalhada: ");
	scanf("%f", &vlrHora);
	
	printf("\nDigite a quantidade de horas trabalhadas: ");
	scanf("%f", &quantHTrabalhada);
	
	float salarioBruto = calcSalario(vlrHora, quantHTrabalhada);
	//Variavel salarioBruto recebe o resultado do calculo dos parâmetros vlrHora e quantHTrabalhada na função calcSalario
	float salarioLiquido = salarioBruto - calcIR(salarioBruto) - calcINSS(salarioBruto);
	//Variável salarioLiquido recebe o resultado do salarioBruto subtraido pelo calculo do parâmetro salarioBruto nas funções calcIR e calcINSS
	
	printf("\nSalário Bruto --> R$ %.2f", salarioBruto);
	//Impressão do resultado do Salario Bruto, dado pela variável salarioBruto
	printf("\nIR --> R$ %.2f", calcIR(salarioBruto));
	//Impressão do resultado do Imposto de Renda, dado pela função calcIR com o parâmetro salarioBruto
	printf("\nINSS --> R$ %.2f", calcINSS(salarioBruto));
	//Impressão do resultado do INSS, dado pela função calcINSS com o parâmetro salarioBruto
	printf("\nFGTS --> R$ %.2f", calcFGTS(salarioBruto));
	//Impressão do resultado do FGTS, dado pela função calcFGTS com o parâmetro salarioBruto
	printf("\nSalário Líquido --> R$ %.2f", salarioLiquido);
	//Impressão do resultado do Salário Líquido, dado pela variável salarioLiquido
	
	return 0;
}

//Função main - Função principal do código, onde iniciará o programa que irá chamar as funções necessárias para iniciar a ordem de lógica das funções
int main(){
	vlrHolerite();
	//Chamada da função vlrHolerite, que solicita valores para chamar outras funções de calculo e imprimir o resultado dos calculos.
	
	return 0;
}