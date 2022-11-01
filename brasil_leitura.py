# importação do Neo4j Driver para o Python
import os
import glob
import ctypes
from heapq import merge
import random
from venv import create
from neo4j import GraphDatabase
import csv
import pandas as pd
from sqlalchemy import table
from tqdm import tqdm

# Credenciais do banco de dados
uri = "bolt://localhost:7687"

userName = "neo4j"

password = "1234"

# Conexão no servidor do banco de dados do Neo4j
db = GraphDatabase.driver(uri, auth=(userName, password))

# CQL para fazer a consulta de todos os lugares presentes no grafo
cqlNodeQuery = "MATCH (br:Brazil) RETURN br"

cqlCreate = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                CREATE (Br:BRAZIL {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,
                countrycode:linha.countrycode, admin4code:linha.admin4code,
                modificationdate:linha.modificationdate, longitude:linha.longitude})

                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname})"""


cqlCreate1 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11})
                
                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other19:othername19{othername19:linha.othername19})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other23:othername123{othername23:linha.othername23})
                
                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername5{othername29:linha.othername29})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35})
                
                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40})


                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11})
                
                
                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11})
                
                
                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11})"""

cqlCreate2 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other0)-[:OTHER_NAME0]->(Br)

                RETURN *;"""

cqlCreate3 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other1)-[:OTHER_NAME1]->(Br)

                RETURN *;"""

cqlCreate4 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other2)-[:OTHER_NAME2]->(Br)

                RETURN *;"""

cqlCreate5 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other3)-[:OTHER_NAME3]->(Br)

                RETURN *;"""

cqlCreate6 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other4)-[:OTHER_NAME4]->(Br)

                RETURN *;"""

cqlCreate7 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other5)-[:OTHER_NAME5]->(Br)

                RETURN *;"""

cqlCreate8 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other6)-[:OTHER_NAME6]->(Br)

                RETURN *;"""

cqlCreate9 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other7)-[:OTHER_NAME7]->(Br)

                RETURN *;"""

cqlCreate10 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other8)-[:OTHER_NAME8]->(Br)

                RETURN *;"""

cqlCreate11 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other9)-[:OTHER_NAME9]->(Br)

                RETURN *;"""

cqlCreate12 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other10)-[:OTHER_NAME10]->(Br)

                RETURN *;"""

cqlCreate13 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (other11)-[:OTHER_NAME11]->(Br)

                RETURN *;"""

cqlCreate14 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha

                MATCH(ascii:ASCIINAME{asciiname: linha.asciiname})
                MATCH(Br:BRAZIL{name:linha.name})

                CREATE (ascii)-[:ASCIINAME]->(Br)

                RETURN *;"""


# Função para criar um arquivo csv com os nomes alternativos separados por colunas
def div_names():
    df = pd.read_csv('BR.csv')
    df = df.join(df['alternatenames'].str.split('$', expand=True).add_prefix('othername'))
    print(df)
    df2 = df.drop('alternatenames', axis = 1)
    df2.to_csv('OtherNames.csv')
div_names()

# Criação dos nós
#with db.session() as graphDB_Session:
#    graphDB_Session.run(cqlCreate)
#    graphDB_Session.run(cqlCreate1)
#    graphDB_Session.run(cqlCreate2)
#    graphDB_Session.run(cqlCreate3)
#    graphDB_Session.run(cqlCreate4)
#    graphDB_Session.run(cqlCreate5)
#    graphDB_Session.run(cqlCreate6)
#    graphDB_Session.run(cqlCreate7)
#    graphDB_Session.run(cqlCreate8)
#    graphDB_Session.run(cqlCreate9)
#    graphDB_Session.run(cqlCreate10)
#    graphDB_Session.run(cqlCreate11)
#    graphDB_Session.run(cqlCreate12)
#    graphDB_Session.run(cqlCreate13)
#    graphDB_Session.run(cqlCreate14)
    #Query do grafo
#    nodes = graphDB_Session.run(cqlNodeQuery)
