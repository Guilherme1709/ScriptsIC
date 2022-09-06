# importação do Neo4j Driver para o Python
import ctypes
from venv import create
from neo4j import GraphDatabase
import csv
import pandas as pd

# Credenciais do banco de dados
uri = "bolt://localhost:7687"

userName = "neo4j"

password = "1234"

# Conexão no servidor do banco de dados do Neo4j
db = GraphDatabase.driver(uri, auth=(userName, password))

# CQL para fazer a consulta de todos os lugares presentes no grafo
cqlNodeQuery = "MATCH (br:Brazil) RETURN br"

#CQL para criar os nós
cqlCreate1 = """LOAD CSV WITH HEADERS FROM 'file:///BR-teste.csv' AS linha

                CREATE (br:BRAZIL {elevation:linha.elevation, featurecode:linha.featurecode, 
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude, 
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population, 
                featureclass:linha.featureclass, cc2:linha.cc2, 
                admin3code:linha.admin3code, name:linha.name, asciiname: linha.asciiname, 
                altenatenames:linha.alternatenames, admin1code:linha.admin1code, 
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})"""

cqlCreate2 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha
                MATCH (linha)
                WHERE linha.id = item.startNode.customId 
                CREATE (othernames:OTHERNAMES {0:linha.0, 1:linha.1, 2:linha.2})"""

#Função para criar um arquivo csv com os nomes alternativos separados por colunas
def div_names():                
    df = pd.read_csv('BR-teste.csv')

    for linha in range(len(df)):
        divisao = df['alternatenames'].str.split('$', expand=True)
    divisao.to_csv("OtherNames.csv", index=False)
div_names()

with db.session() as graphDB_Session:

    #Criação dos nós
    #graphDB_Session.run(cqlCreate1)
    graphDB_Session.run(cqlCreate2)
    #graphDB_Session.run(cqlCreate3)
    #Query do grafo
    nodes = graphDB_Session.run(cqlNodeQuery)

    #print("Lista de lugares presentes no grafo")
    for node in nodes:
        print(node)

