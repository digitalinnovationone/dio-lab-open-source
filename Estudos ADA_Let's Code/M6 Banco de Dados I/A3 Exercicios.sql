/*Na aula anterior vimos sobre tipos de variaveis e começamos a fazer consultas...vamos intensificar*/

/* SELECT SINTAXE */

SELECT column1, column2, ...
FROM table_name;

SELECT city FROM customers;
SELECT * FROM customers;

Professor: 

--Exercicios:
-- 1) SELECIONE TODAS AS COLUNAS DA TABELA CUSTOMERS.
-- 2) Por que utilizar Select *  nem sempre é recomendavel?
-- 3) Selecione Contact_name e contact_title da tabela CUSTOMERS.


/* SELECT DISTINCT */

SELECT DISTINCT column1, column2, ...
FROM table_name;

-- 4) selecione os distintos title_of_courtesy da tabela employees


/* SELECT LIMIT */

SELECT column_name(s)
FROM table_name
LIMIT number;

-- 5 ) SELECIONE 100 LINHAS DA TABELA ORDERS.

/* Select COUNT() */
 SELECT COUNT(column_name)
FROM table_name

-- 6) SELECIONE A QUANTIDADE TOTAL DE LINHAS DA TABELA ORDERS


/* SELECT AVG ()*/

SELECT AVG(column_name)
FROM table_name


/*SELECT SUM()*/

SELECT SUM(column_name)
FROM table_name


/* SELECT MAX () MIN() */
SELECT MIN(column_name) -- MAX()
FROM table_name

-- 7) SELECIONE A MEDIA DO FREIGHT, DEPOIS A SOMA TOTAL, DEPOIS O VALOR MAXIMO DA TABELA ORDERS.


/* WHERE */ 

SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- operadores:
 = igual
 > maior que 
 < menor que
 >=  <=  maior igual ou menor igual
 <> ou !=  diferente de 
 BETWEEN  (entre valores)
 LIKE (procura por um padrão) https://www.postgresql.org/docs/9.0/functions-matching.html
 IN  ou NOT IN ( multiplos valores para uma mesma coluna)
 IS NULL é nulo
 IS NOT NULL não é nulo
 OR
 AND
 
 -- 8) SELECIONAR OS REGISTROS DA TABELAS ORDERS ONDE O FREIGHT FOI MAIOR QUE 50 E REQUIRED_DATE FOI DEPOIS A PARIR DO DIA 01-01-2017
	
 -- 9) SELECIONAR DA TABELA ORDERS , todos os requirementos (required_date) entre 01-01-1997 e 01-01-1998 E que tinha ship_adress começando com a palavara rua


/* ORDER BY */ 

SELECT column1, column2, ...
FROM table_name
WHERE condition...
ORDER BY column1, column2, ... ASC|DESC;


 /* Create table */
 
 CREATE TABLE table_name
    AS query

-- 10 ) Crie uma nova tabela chamada  orders_rua  a partir do exercicio 9

-- 11) verifique quantas linhas tem essa tabela, sem precisar consultar os dados.

 /* Create view */
 https://www.postgresql.org/docs/9.2/sql-createview.html
 
-- 12) explique a diferença entre criar uma tabela e uma view, caso nao saiba ingles, que é o caso da documentação, pode pesquisar em qualquer site.

-- 13) Crie uma view com a mesma query do exercicio 9


/*DROP TABLE/VIEW*/

DROP TABLE TABLE_NAME;

-- 14) DELETE A VIEW QUE CRIAMOS .
https://www.postgresql.org/docs/9.4/sql-dropview.html

/*DELETE TABLE*/

DELETE FROM table_name WHERE condition;

--15) crie a cópia da tabela orders,apenas onde o pais (country) é brazil e depois delete todos os registros que não forem de São Paulo (ship_region)

--16 ) como verificar se o que voce fez esta correto?


/*UPDATE*/

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

-- 17) Fomos informado que agora a cidade de rezende, mudou de nome e se chama São Paulo. Realize esse update.




/* Na proxima aula: 
	FUNÇÕES DE TEXTO,UPPER,LOWER,CAST,UNION, group by, having, insert into, Joins *
	




