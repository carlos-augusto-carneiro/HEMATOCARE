-- Criação da tabela Ponto de coleta
CREATE TABLE Ponto_de_coleta (
    CNPJ VARCHAR(14) PRIMARY KEY,
    Email VARCHAR(100),
    Nome VARCHAR(100),
    Segmento VARCHAR(100),
    Logradouro VARCHAR(100),
    Numero VARCHAR(10),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    CEP VARCHAR(8)
);

-- Criação da tabela Doador
CREATE TABLE Doador (
    CPF VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(100),
    Idade INTEGER,
    Email VARCHAR(100),
    Logradouro VARCHAR(100),
    Numero VARCHAR(10),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    CEP VARCHAR(8),
    Tipo_sanguineo VARCHAR(5),
    Senha VARCHAR(255) NOT NULL
);

-- Criação da tabela Telefone_Doador
CREATE TABLE Telefone_Doador (
    CPF VARCHAR(11) REFERENCES Doador(CPF),
    Numero VARCHAR(20),
    PRIMARY KEY (CPF, Numero)
);

-- Criação da tabela Bolsa de sangue
CREATE TABLE Bolsa_de_sangue (
    Codigo_bolsa_sangue SERIAL PRIMARY KEY,
    CPF VARCHAR(11) REFERENCES Doador(CPF),
    Data DATE,
    CNPJ VARCHAR(14) REFERENCES Ponto_de_coleta(CNPJ)
);

-- Criação da tabela Hospital
CREATE TABLE Hospital (
    CNPJ VARCHAR(14) PRIMARY KEY,
    Email VARCHAR(100),
    Nome VARCHAR(100),
    Logradouro VARCHAR(100),
    Numero VARCHAR(10),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    CEP VARCHAR(8)
);

-- Criação da tabela Telefone_Hospital
CREATE TABLE Telefone_Hospital (
    CNPJ VARCHAR(14) REFERENCES Hospital(CNPJ),
    Numero VARCHAR(20),
    PRIMARY KEY (CNPJ, Numero)
);

-- Criação da tabela Recebe
CREATE TABLE Recebe (
    CNPJ VARCHAR(14) REFERENCES Hospital(CNPJ),
    Codigo_bolsa_sangue INTEGER REFERENCES Bolsa_de_sangue(Codigo_bolsa_sangue),
    Data DATE,
    Hora TIME,
    PRIMARY KEY (CNPJ, Codigo_bolsa_sangue)
);

-- Criação da tabela Telefone_Ponto_de_coleta
CREATE TABLE Telefone_Ponto_de_coleta (
    CNPJ_Ponto_de_coleta VARCHAR(14) REFERENCES Ponto_de_coleta(CNPJ),
    Numero VARCHAR(20),
    PRIMARY KEY (CNPJ_Ponto_de_coleta, Numero)
);

-- Criação da tabela Funcionario
CREATE TABLE Funcionario (
    Codigo_fun SERIAL PRIMARY KEY,
    Nome VARCHAR(100),
    CRM VARCHAR(20),
    COREN VARCHAR(20)
);

-- Criação da tabela Atender
CREATE TABLE Atender (
    Codigo_fun INTEGER REFERENCES Funcionario(Codigo_fun),
    CPF_doador VARCHAR(11) REFERENCES Doador(CPF),
    PRIMARY KEY (Codigo_fun, CPF_doador)
);
