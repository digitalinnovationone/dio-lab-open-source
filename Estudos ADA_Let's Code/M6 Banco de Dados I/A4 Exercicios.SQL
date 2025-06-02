
DROP TABLE  /*IF EXISTS*/ top_jogadores_fifa;

CREATE TABLE top_jogadores_fifa(
	nome_do_jogador VARCHAR NOT NULL,
	ano_premiacao SMALLINT
);

DROP TABLE  /*IF EXISTS*/ top_jogadores_popularidade;

CREATE TABLE top_jogadores_popularidade(
	nome_do_jogador VARCHAR NOT NULL,
	ano_premiacao SMALLINT
);

INSERT INTO top_jogadores_fifa (nome_do_jogador,ano_premiacao)
VALUES
	('Alexia Putellas',2021),
	('Robert_Lewandowski',2021),
	('Lucy Bronze',2020),
	('Robert_Lewandowski',2020);

INSERT INTO top_jogadores_popularidade (nome_do_jogador,ano_premiacao)
VALUES
	('Neymar',2021),
	('Marta',2021),
	('Robert_Lewandowski',2020);
	
-- UNION ( UNION ALL)
/* Exercicio 1: Faça uma query, que retorne em apenas uma tabela, 
os jogadores e ano de premiação, tanto pela fifa quanto em popularidade*/

SELECT /*[columns...]*/ FROM /*[table]*/
UNION -- OU UNION ALL
SELECT /*[columns...]*/ FROM /*[table]*/

-- Exercicio 2: qual a diferença entre Union e Union ALL


/*INSERT INTO SELECT*/

CREATE TABLE TOP_JOGADORES AS 
	SELECT 
		*
	FROM top_jogadores_fifa;
	
-- SYNTAXE: 
INSERT INTO /*TABLE2*/ SELECT * FROM /*TABLE1*/ 

-- Exercicio 3: insira os valores da tabela top_jogadores_popularidade
-- na tabela TOP_JOGADORES.


-- Exercicio 4: para criar a tabela TOP_JOGADORES, existiam varias alternativas
-- construa as que você conseguiu imaginar.

/* GROUP BY */

SELECT column1,avg(column2) FROM table1 GROUP BY column1

/* funçoes de agregacao: avg,sum,count(*),etc*/

-- na tabela premio fifa, mostre quantas vezes o jogador ganhou o premio

SELECT 
	nome_do_jogador,
	count(*) AS quantidade
FROM top_jogadores_fifa
GROUP BY nome_do_jogador
ORDER BY quantidade DESC;

-- Exercicio 5: na tabela orders, selecione a média do freight pago para cada ship_country
-- relatorio : ship_cuntry , media_frete

SELECT ship_country,avg(freight) from orders group by ship_country

-- Exrcicio 6: agora mostre a quantidade de pedidos que são feitos por cidade e por pais.
-- relatorio: ship_country,ship_city,quantidade_de_pedidos
/*
	CHAVE PRIMARIA - PRIMARY KEY: COLUNA, OU CONJUNTO DE COLUNAS, QUE GARANTE OS SEGUINTES
		OBJETIVOS
		- NÃO HAVER DUPLICAÇÃO
		- O REGISTRO NÃO PODE SER NULO
	SÓ PODE HAVER UMA CHAVE PRIMARIA POR TABELA.
	
	CHAVE ESTRANGEIRA - FOREIGN KEY (FK)
		- RELACIONAMENTO ENTRE TABELAS!
		- IMPEDIR O DESCASAMENTO DE INFORMAÇÕES, EM UM BANCO DE DADOS:
			-IMPEDE QUE VOCE EXLUA UM REGISTRO CASO ELE FAÇA REFERENCIA A OUTRA TABELA
			-IMPEDE QUE VOCÊ INSIRA VALORES INVALIDOS NO ID DE UMA TABELA
	
	CHAVE PRIMARIA - IDENTIFICA
	CHAVE ESTRANGEIRA - RELACIONA

*/


/* JOINS */

/* INNER JOIN : RETORNA OS REGISTROS QUE EXISTEM EM AMBAS AS TABELAS
   LEFT JOIN: RETORNA TODAS AS LINHAS DA TABELA DA ESQUERDA + AS LINHAS 
   			  QUE DÃO MATCH DA TABELA DA DIREITA
   RIGT JOIN: CONTRARIO DO LEFT JOIN
   FULL JOIN: RETORNA TODAS AS LINHAS, TANTO DA ESQUERDA, QUANTO DA DIREITA, QUANDO DA MATCH.
   */
   
   -- EXEMPLO DE QUERY
	SELECT 
		A.PRODUCT_ID,
		A.PRODUCT_NAME,
		B.QUANTITY
	 FROM PRODUCTS AS A
	 LEFT JOIN ORDER_DETAILS AS B
	 ON A.PRODUCT_ID = B.PRODUCT_ID

-- TABELAS PARA ABSTRAÇÃO DOS CONCEITOS:

CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');

-- INNER JOIN:
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
INNER JOIN basket_b
    ON fruit_a = fruit_b;
	
-- LEFT JOIN:

SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b 
   ON fruit_a = fruit_b;
   
 -- LEFT JOIN (DADOS QUE NAO EXISTEM NA B)
 
 SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b 
    ON fruit_a = fruit_b
WHERE b IS NULL;

-- RIGHT JOIN:
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
RIGHT JOIN basket_b ON fruit_a = fruit_b;

SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
RIGHT JOIN basket_b 
   ON fruit_a = fruit_b
WHERE a IS NULL;

-- FULL [OUTER] JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL  JOIN basket_b 
    ON fruit_a = fruit_b;
	

SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL JOIN basket_b 
   ON fruit_a = fruit_b
WHERE a IS NULL OR b IS NULL;


-- EXERCICIO 7:
-- RELATORIO: Contact_Name,Company_Name,City,OrderID,ORDER_DATE,REQUIRED_DATE
-- TABELAS ENVOLVIDAS: customers e orders
-- DICA: PROCURE OS CAMPOS QUE COEXISTEM NAS DUAS TABELAS, OU O CONCEITO DE PRIMARY KEY


-- VAMOS FALAR MAIS A RESPEITO DAS CHAVES!!


	







