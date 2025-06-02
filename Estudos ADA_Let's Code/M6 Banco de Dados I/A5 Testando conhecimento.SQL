 /* Case simples */

 case search-expression
   when expression_1 [, expression_2, ...] then
      when-statementsv
  [ ... ]
  [else
      else-statements ]
END case;

/* Exemplo case */

SELECT
	ORDER_ID,
	FREIGHT,
	CASE
		WHEN FREIGHT > 10 AND FREIGHT <= 20 THEN '>10'
		WHEN FREIGHT > 20 AND FREIGHT <= 30 THEN '>20'
		WHEN FREIGHT > 30 THEN 'Esquece'
	END "FLAG"
	FROM ORDERS;

/* COALESCE */

SELECT
	COALESCE (1, 2);
	
SELECT
	COALESCE (NULL, 2 , 1);


CREATE TABLE items (
	ID serial PRIMARY KEY,
	product VARCHAR (100) NOT NULL,
	price NUMERIC NOT NULL,
	discount NUMERIC
);

INSERT INTO items (product, price, discount)
VALUES
	('A', 1000 ,10),
	('B', 1500 ,20),
	('C', 800 ,5),
	('D', 500, NULL);
	
SELECT
	product,
	(price - discount) AS net_price
FROM
	items;
	
SELECT
	product,
	(price - COALESCE(discount,0)) AS net_price
FROM
	items;
	
SELECT
	product,
	(
		price - CASE
		WHEN discount IS NULL THEN
			0
		ELSE
			discount
		END
	) AS net_price
FROM
	items;

/* SUBQUERY */

SELECT AVG(UNIT_PRICE) FROM ORDER_DETAILS;

select * from order_details WHERE UNIT_PRICE > (SELECT AVG(UNIT_PRICE) FROM ORDER_DETAILS );

/* CONCAT */
CONCAT(str_1, str_2, ...)

SELECT
	CONCAT ('Matheus',' ', 'Araujo');

SELECT CONCAT(FIRST_NAME,LAST_NAME) FROM EMPLOYEES;

SELECT CONCAT_WS(' ',FIRST_NAME,LAST_NAME) FROM EMPLOYEES;

/* LEFT*/

SELECT LEFT ('Matheus',2)

/*Length*/

SELECT LENGTH('ABC');

/* lOWER E UPPER - ja viram*/

/*TRIM*/

SELECT TRIM('       MATHEUS')

/* e uma infinidade mais...*/


/* CAST */

SELECT
	CAST ('100' AS INTEGER);

SELECT
	CAST ('10C' AS INTEGER);

SELECT
   CAST ('2015-01-01' AS DATE),
   CAST ('01-OCT-2015' AS DATE);

SELECT
   CAST ('10.2' AS DOUBLE PRECISION);

   SELECT 
   CAST('true' AS BOOLEAN),
   CAST('false' as BOOLEAN),
   CAST('T' as BOOLEAN),
   CAST('F' as BOOLEAN);


CREATE TABLE TESTE_MATH (COLUNA_A VARCHAR )

INSERT INTO TESTE_MATH (COLUNA_A)
VALUES
	('1'),
	('2'),
	('3');
	
SELECT SUM(CAST(COLUNA_A AS INTEGER)) FROM TESTE_MATH


/* TRUNC*/

TRUNC(number [, precision])

/* ABS*/

ABS(numeric_expression)
SELECT ABS( 100 - 250 );

/*CEIL - FLOOR*/

SELECT
    CEIL( 200.25 );

/*ROUND*/
ROUND (source [ , n ] )

SELECT
    ROUND( 10.812, 2 );

SELECT
    ROUND( 10.812 );

SELECT
    FLOOR( 10.812 );


-- URI 2602

CREATE TABLE customers (
  id NUMERIC PRIMARY KEY,
  name CHARACTER VARYING (255),
  street CHARACTER VARYING (255),
  city CHARACTER VARYING (255),
  state CHAR (2),
  credit_limit NUMERIC
);

INSERT INTO customers (id, name, street, city, state, credit_limit)
VALUES 
  (1,	'Pedro Augusto da Rocha',	'Rua Pedro Carlos Hoffman',	'Porto Alegre',	'RS',	700.00),
  (2,	'Antonio Carlos Mamel',	'Av. Pinheiros', 'Belo Horizonte',	'MG',	3500.50),
  (3,	'Luiza Augusta Mhor',	'Rua Salto Grande',	'Niteroi',	'RJ',	4000.00),	
  (4,	'Jane Ester',	'Av 7 de setembro',	'Erechim',	'RS',	800.00),
  (5, 'Marcos Antônio dos Santos',	'Av Farrapos',	'Porto Alegre',	'RS',	4250.25);

-- URI 2603 

CREATE TABLE customers (
  id NUMERIC PRIMARY KEY,
  name CHARACTER VARYING (255),
  street CHARACTER VARYING (255),
  city CHARACTER VARYING (255),
  state CHAR (2),
  credit_limit NUMERIC
);

INSERT INTO customers (id, name, street, city, state, credit_limit)
VALUES
  (1,	'Pedro Augusto da Rocha',	'Rua Pedro Carlos Hoffman',	'Porto Alegre',	'RS',	700.00),
  (2,	'Antonio Carlos Mamel',	'Av. Pinheiros',	'Belo Horizonte',	'MG',	3500.50),	
  (3,	'Luiza Augusta Mhor,',	'Rua Salto Grande',	'Niteroi',	'RJ',	4000.00),
  (4,	'Jane Ester',	'Av 7 de setembro',	'Erechim',	'RS',	800.00),
  (5,	'Marcos Antônio dos Santos',	'Av Farrapos',	'Porto Alegre',	'RS',	4250.25);

  -- 2604


CREATE TABLE products (
  id NUMERIC PRIMARY KEY,
  name CHARACTER VARYING (255),
  amount NUMERIC,
  price NUMERIC
);

INSERT INTO products (id, name, amount, price)
VALUES 
  (1,	'Two-door wardrobe',	100,	80),
  (2,	'Dining table',	1000,	560),
  (3,	'Towel holder',	10000,	5.50),
  (4,	'Computer desk',	350,	100),
  (5,	'Chair',	3000,	210.64),
  (6,	'Single bed',	750,	99);
  

  -- 2605

  CREATE TABLE categories (
  id numeric PRIMARY KEY,
  name varchar
);

CREATE TABLE providers (
  id numeric PRIMARY KEY,
  name varchar(50),
  street varchar(50),
  city varchar(50),
  state varchar(2)
);

CREATE TABLE products (
  id numeric PRIMARY KEY,
  name varchar(50),
  amount numeric,
  price numeric(7,2),
  id_providers numeric REFERENCES providers (id),
  id_categories numeric REFERENCES categories (id)
);


INSERT INTO categories (id , name)
VALUES 
  (1,	'old stock'),
  (2,	'new stock'),
  (3,	'modern'),
  (4,	'commercial'),
  (5,	'recyclable'),
  (6,	'executive'),
  (7,	'superior'),
  (8,	'wood'),
  (9,	'super luxury'),
  (10,	'vintage');
  
INSERT INTO providers (id, name, street, city, state)
VALUES 
  (1,	'Henrique'	,'Av Brasil',	'Rio de Janeiro',	'RJ'),
  (2,	'Marcelo Augusto',	'Rua Imigrantes',	'Belo Horizonte',	'MG'),
  (3,	'Caroline Silva', 'Av São Paulo',	'Salvador',	'BA'),
  (4,	'Guilerme Staff',	'Rua Central',	'Porto Alegre',	'RS'),
	(5,	'Isabela Moraes',	'Av Juiz Grande',	'Curitiba',	'PR'),
  (6,	'Francisco Accerr',	'Av Paulista',	'São Paulo',	'SP');
  
INSERT INTO products (id, name, amount, price, id_providers, id_categories)
VALUES
  (1,	'Two-door wardrobe',	100,	800,	6,	8),
  (2,	'Dining table',	1000,	560,	1,	9),	
  (3,	'Towel holder',	10000,	25.50,	5,	1),
  (4,	'Computer desk',	350,	320.50,	4,	6),
  (5,	'Chair',	3000,	210.64,	3,	6),
  (6,	'Single bed',	750,	460,	1,	2);
  
-- 2606


CREATE TABLE categories (
  id numeric PRIMARY KEY,
  name varchar
);

CREATE TABLE products (
  id numeric PRIMARY KEY,
  name varchar(50),
  amount numeric,
  price numeric(7,2),
  id_categories numeric REFERENCES categories (id)
);


INSERT INTO categories (id, name)
VALUES 
  (1,	'old stock'),
  (2,	'new stock'),
  (3,	'modern'),
  (4,	'commercial'),
  (5,	'recyclable'),
  (6,	'executive'),
  (7,	'superior'),
  (8,	'wood'),
  (9,	'super luxury'),
  (10,	'vintage');
  
INSERT INTO products (id , name, amount, price, id_categories)
VALUES
  (1,	'Lampshade',	100,	800,	4),
  (2,	'Table for painting',	1000,	560,	9),
  (3,	'Notebook desk',	10000,	25.50,	9),
  (4,	'Computer desk',	350,	320.50,	6),
  (5,	'Chair',	'3000',	'210.64',	9),	
  (6,	'Home alarm',	750,	460,	4);


  -- 2607


CREATE TABLE providers (
  id numeric PRIMARY KEY,
  name varchar(50),
  street varchar(50),
  city varchar(50),
  state varchar(2)
);

INSERT INTO providers (id, name, street, city, state)
VALUES 
  (1,	'Henrique',	'Av Brasil',	'Rio de Janeiro',	'RJ'),
  (2,	'Marcelo Augusto',	'Rua Imigrantes',	'Belo Horizonte',	'MG'),
  (3,	'Caroline Silva',	'Av São Paulo',	'Salvador',	'BA'),
  (4,	'Guilerme Staff',	'Rua Central',	'Porto Alegre',	'RS'),
  (5,	'Isabela Moraes',	'Av Juiz Grande',	'Curitiba',	'PR'),
  (6,	'Francisco Accerr',	'Av Paulista',	'São Paulo',	'SP');

  --2608

  CREATE TABLE products (
  id numeric PRIMARY KEY,
  name varchar(50),
  amount numeric,
  price numeric(7,2)
);

INSERT INTO products (id, name, amount, price)
VALUES
  (1,	'Two-doors wardrobe',	100,	800),
  (2,	'Dining table',	1000,	560),
  (3,	'Towel holder',	10000,	25.50),
  (4,	'Computer desk',	350,	320.50),
  (5,	'Chair',	3000,	210.64),
  (6,	'Single bed',	750,	460);
  

  -- 2609

  CREATE TABLE categories (
  id numeric PRIMARY KEY,
  name varchar
);

CREATE TABLE products (
  id numeric PRIMARY KEY,
  name varchar(50),
  amount numeric,
  price numeric(7,2),
  id_categories numeric REFERENCES categories (id)
);

INSERT INTO categories (id, name)
VALUES 
  (1,	'wood'),
  (2,	'luxury'),
  (3,	'vintage'),
  (4,	'modern'),
  (5,	'super luxury');
  
INSERT INTO products (id, name, amount, price, id_categories)
VALUES 
  (1,	'Two-doors wardrobe', 100,	800,	1),
  (2,	'Dining table',	1000,	560,	3),
  (3,	'Towel holder',	10000,	25.50,	4),
  (4,	'Computer desk',	350,	320.50,	2),
  (5,	'Chair',	3000,	210.64,	4),
  (6,	'Single bed',	750,	460,	1);

  --2610

  CREATE TABLE products (
    id NUMERIC PRIMARY KEY,
    name VARCHAR,
    amount NUMERIC,
    price NUMERIC
);

INSERT INTO products (id, name, amount, price)
VALUES
    (1, 'Two-doors wardrobe', 100, 800),
    (2, 'Dining table', 1000, 560),
    (3, 'Towel holder', 10000, 25.50),
    (4, 'Computer desk', 350, 320.50),
    (5, 'Chair', 3000, 210.64),
    (6, 'Single bed', 750, 460);


    -- 2611

    CREATE TABLE genres (
  id numeric PRIMARY KEY,
  description varchar(50)
);

CREATE TABLE movies (
  id numeric PRIMARY KEY,
  name varchar(50),
  id_genres numeric REFERENCES genres (id)
);

INSERT INTO genres (id, description)
VALUES
  (1,	'Animation'),
  (2,	'Horror'),
  (3,	'Action'),
  (4,	'Drama'),
  (5,	'Comedy');
  
INSERT INTO movies (id, name, id_genres)
VALUES
  (1,	'Batman',	3),
  (2,	'The Battle of the Dark River',	3),
  (3,	'White Duck',	1),
  (4,	'Breaking Barriers',	4),
  (5,	'The Two Hours',	2);


-- 2612


CREATE TABLE genres (
  id numeric PRIMARY KEY,
  description varchar(50)
);

CREATE TABLE movies (
  id numeric PRIMARY KEY,
  name varchar(50),
  id_genres numeric REFERENCES genres (id)
);

CREATE TABLE actors (
  id numeric PRIMARY KEY,
  name varchar(50)
);

CREATE TABLE movies_actors (
  id_movies numeric REFERENCES movies (id),
  id_actors numeric REFERENCES actors (id)
); 

INSERT INTO genres (id, description)
VALUES
  (1,	'Animation'),
  (2,	'Horror'),
  (3,	'Action'),
  (4,	'Drama'),
  (5,	'Comedy');
  
INSERT INTO movies (id, name, id_genres)
VALUES
  (1,	'Batman',	3),
  (2,	'The Battle of the Dark River',	3),
  (3,	'White Duck',	1),
  (4,	'Breaking Barriers',	4),
  (5,	'The Two Hours',	2);
  
INSERT INTO actors (id, name)
VALUES
  (1,	'Brad Antonio'),
  (2,	'Marcelo Silva'),
  (3,	'Miguel Silva'),
  (4,	'Drake Frost'),
  (5,	'Rodrigo Juares Rodriguez');
    
INSERT INTO movies_actors (id_movies, id_actors)
VALUES
  (1,1),
  (2,3),
  (2,2),
  (4,1),
  (5,2);

  -- 2614


CREATE TABLE prices (
  id numeric PRIMARY KEY,
  categorie varchar(50),
  value numeric
);


CREATE TABLE movies (
  id numeric PRIMARY KEY,
  name varchar(50),
  id_prices numeric REFERENCES prices (id)
);

INSERT INTO prices (id , categorie, value)
VALUES
  (1,	'Releases',	3.50),
  (2,	'Bronze Seal',	2.00),
  (3,	'Silver Seal',	2.50),
  (4,	'Gold Seal',	3.00),
  (5,	'Promotion',	1.50);
  
INSERT INTO movies (id, name, id_prices)
VALUES
  (1,	'Batman',	3),
  (2,	'The Battle of the Dark River',	3),
  (3,	'White Duck',	5),
  (4,	'Breaking Barriers',	4),
  (5,	'The Two Hours',	2);