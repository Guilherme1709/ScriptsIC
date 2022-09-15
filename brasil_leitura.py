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
                modificationdate:linha.modificationdate, longitude:linha.longitude, 
                other_names:linha.other_names, other_names1:linha.other_names1, other_names2:linha.other_names2})"""


cqlCreate2 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                CREATE (Br:BRAZIL {elevation:linha.elevation, featurecode:linha.featurecode, 
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude, 
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population, 
                featureclass:linha.featureclass, cc2:linha.cc2, 
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code, 
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.other_names IS null
                CREATE (other:OTHER_NAMES{other_names:linha.other_names})

                WITH linha WHERE NOT linha.other_names1 IS null
                CREATE (other1:OTHER_NAMES1{other_names1:linha.other_names1})

                WITH linha WHERE NOT linha.other_names2 IS null
                CREATE (other2:OTHER_NAMES2{other_names2:linha.other_names2})

                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname})"""


cqlCreate3 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other:OTHER_NAMES{other_names:linha.other_names})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other)-[:OTHER_NAME]->(Br)

                RETURN *;"""


cqlCreate4 =  """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other1:OTHER_NAMES1{other_names1:linha.other_names1})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other1)-[:OTHER_NAME1]->(Br)

                RETURN *;"""


cqlCreate5 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other2:OTHER_NAMES2{other_names2:linha.other_names2})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other2)-[:OTHER_NAME2]->(Br)

                RETURN *;"""


cqlCreate6 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(ascii:ASCIINAME{asciiname: linha.asciiname})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (ascii)-[:ASCIINAME]->(Br)

                RETURN *;"""


#Função para criar um arquivo csv com os nomes alternativos separados por colunas
def div_names():                
    df = pd.read_csv('BR-teste.csv')

    for linha in range(len(df)):
        df[['other_names', 'other_names1', 'other_names2']] = df['alternatenames'].str.split('$', expand=True)

    df.drop(columns=["alternatenames"], inplace=True)

    df.to_csv("OtherNames.csv", index=False)
#div_names()


#Criação dos nós
with db.session() as graphDB_Session:
    #graphDB_Session.run(cqlCreate1)
    #graphDB_Session.run(cqlCreate2)
    graphDB_Session.run(cqlCreate3)
    graphDB_Session.run(cqlCreate4)
    graphDB_Session.run(cqlCreate5)
    graphDB_Session.run(cqlCreate6)
    #Query do grafo
    nodes = graphDB_Session.run(cqlNodeQuery)


