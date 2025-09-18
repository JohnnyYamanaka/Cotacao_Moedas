SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;



SET default_tablespace = '';

SET default_with_oids = false;

CREATE DATABASE cotacoes;

\connect cotacoes

DROP TABLE IF EXISTS silver_usd_cotacao;
DROP TABLE IF EXISTS silver_eur_cotacao;
DROP TABLE IF EXISTS silver_gbp_cotacao;
DROP TABLE IF EXISTS silver_jpy_cotacao;


CREATE TABLE silver_usd_cotacao (
    cotacao_compra REAL NOT NULL CHECK (cotacao_compra > 0),
    cotacao_venda REAL NOT NULL CHECK(cotacao_venda > 0),
    data_cotacao date NOT NULL,
    hora_cotacao time NOT NULL,
    PRIMARY KEY (data_cotacao, hora_cotacao)
);

CREATE TABLE silver_eur_cotacao (
    cotacao_compra REAL NOT NULL CHECK (cotacao_compra > 0),
    cotacao_venda REAL NOT NULL CHECK(cotacao_venda > 0),
    data_cotacao date NOT NULL,
    hora_cotacao time NOT NULL,
    PRIMARY KEY (data_cotacao, hora_cotacao)
);

CREATE TABLE silver_gbp_cotacao (
    cotacao_compra REAL NOT NULL CHECK (cotacao_compra > 0),
    cotacao_venda REAL NOT NULL CHECK(cotacao_venda > 0),
    data_cotacao date NOT NULL,
    hora_cotacao time NOT NULL,
    PRIMARY KEY (data_cotacao, hora_cotacao)
);

CREATE TABLE silver_jpy_cotacao (
    cotacao_compra REAL NOT NULL CHECK (cotacao_compra > 0),
    cotacao_venda REAL NOT NULL CHECK(cotacao_venda > 0),
    data_cotacao date NOT NULL,
    hora_cotacao time NOT NULL,
    PRIMARY KEY (data_cotacao, hora_cotacao)
);

CREATE INDEX idx_data_cotacao_usd ON silver_usd_cotacao (data_cotacao);
CREATE INDEX idx_data_cotacao_eur ON silver_eur_cotacao (data_cotacao);
CREATE INDEX idx_data_cotacao_gbp ON silver_gbp_cotacao (data_cotacao);
CREATE INDEX idx_data_cotacao_jpy ON silver_jpy_cotacao (data_cotacao);
