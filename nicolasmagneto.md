-- CREATE TABLES for ecommerce_db
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

-- ====================
-- Clientes (base)
-- ====================
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefone VARCHAR(20),
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Cliente PF (especialização)
CREATE TABLE clientes_pf (
    id_cliente INT PRIMARY KEY,
    cpf CHAR(11) UNIQUE NOT NULL,
    data_nascimento DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE
);

-- Cliente PJ (especialização)
CREATE TABLE clientes_pj (
    id_cliente INT PRIMARY KEY,
    cnpj CHAR(14) UNIQUE NOT NULL,
    razao_social VARCHAR(200),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE
);

-- ====================
-- Vendedores
-- ====================
CREATE TABLE vendedores (
    id_vendedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_vendedor VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE
);

-- ====================
-- Fornecedores
-- ====================
CREATE TABLE fornecedores (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_fornecedor VARCHAR(150) NOT NULL,
    cnpj CHAR(14) UNIQUE
);

-- ====================
-- Produtos
-- ====================
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(200) NOT NULL,
    descricao TEXT,
    preco DECIMAL(12,2) NOT NULL,
    estoque INT DEFAULT 0
);

-- Tabela N:M produtos_fornecedores
CREATE TABLE produtos_fornecedores (
    id_produto INT NOT NULL,
    id_fornecedor INT NOT NULL,
    PRIMARY KEY (id_produto, id_fornecedor),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto) ON DELETE CASCADE,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor) ON DELETE CASCADE
);

-- ====================
-- Pedidos
-- ====================
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_vendedor INT NULL,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
    status_pedido VARCHAR(50) DEFAULT 'Pendente',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id_vendedor)
);

-- Tabela N:M pedidos_produtos (itens do pedido)
CREATE TABLE pedidos_produtos (
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    preco_unitario DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- ====================
-- Pagamentos (um pedido pode ter várias formas/pagamentos)
-- ====================
CREATE TABLE pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    tipo_pagamento VARCHAR(50) NOT NULL, -- Ex: Cartão, Boleto, PIX
    detalhes VARCHAR(255), -- ex: última 4 dígitos do cartão ou banco
    valor DECIMAL(12,2) NOT NULL,
    data_pagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE
);

-- ====================
-- Entregas (status e código de rastreio)
-- ====================
CREATE TABLE entregas (
    id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    status_entrega VARCHAR(50) DEFAULT 'Aguardando',
    codigo_rastreio VARCHAR(100),
    data_prevista DATE,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE
);

-- ====================
-- Triggers to ensure a client is PF OR PJ (but not both)
-- ====================
DELIMITER //
CREATE TRIGGER trg_before_insert_pf
BEFORE INSERT ON clientes_pf
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM clientes_pj WHERE id_cliente = NEW.id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente já cadastrado como PJ';
    END IF;
END;
//

CREATE TRIGGER trg_before_insert_pj
BEFORE INSERT ON clientes_pj
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM clientes_pf WHERE id_cliente = NEW.id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente já cadastrado como PF';
    END IF;
END;
//

CREATE TRIGGER trg_before_update_pf
BEFORE UPDATE ON clientes_pf
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM clientes_pj WHERE id_cliente = NEW.id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Atualização inválida: cliente presente em PJ';
    END IF;
END;
//

CREATE TRIGGER trg_before_update_pj
BEFORE UPDATE ON clientes_pj
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM clientes_pf WHERE id_cliente = NEW.id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Atualização inválida: cliente presente em PF';
    END IF;
END;
//
DELIMITER ;

-- Indexes (opcionais para performance)
CREATE INDEX idx_pedidos_cliente ON pedidos(id_cliente);
CREATE INDEX idx_pedidos_data ON pedidos(data_pedido);
CREATE INDEX idx_produtos_fornecedor ON produtos_fornecedores(id_fornecedor);
