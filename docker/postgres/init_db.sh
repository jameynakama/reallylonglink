#!/usr/bin/env bash

echo "***** Creating hstore extension *****"
gosu postgres psql --dbname template1 <<- EOSQL
    CREATE EXTENSION hstore;
    DROP DATABASE postgres;
    CREATE DATABASE postgres TEMPLATE template1;
EOSQL

echo "***** Creating reallylonglink DB *****"
gosu postgres psql <<- EOSQL
    CREATE USER reallylonglink WITH PASSWORD 'password';
    ALTER USER reallylonglink CREATEDB;
    CREATE DATABASE reallylonglink;
    GRANT ALL PRIVILEGES ON DATABASE reallylonglink TO reallylonglink;
EOSQL
