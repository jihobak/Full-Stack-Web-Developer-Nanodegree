-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
DROP TABLE IF EXISTS Players;

CREATE TABLE Players ( id serial PRIMARY KEY,
                       name VARCHAR (50) NOT NULL,
                       win int DEFAULT 0,
                       lose int DEFAULT 0,
                       matches int DEFAULT 0);
