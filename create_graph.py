import os
import glob
import ctypes
from heapq import merge
import random
import shapely.wkt
from venv import create
from neo4j import GraphDatabase
import csv
import pandas as pd
from sqlalchemy import table
from tqdm import tqdm


# Credentials of the data base
uri = "bolt://localhost:7687"

userName = "neo4j"

password = "12345678"

# Conection with the data base
db = GraphDatabase.driver(uri, auth=(userName, password))

# Queries to create nodes and relationships

cqlCreate0 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""


cqlCreate1 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate2 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate3 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate4 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate5 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate6 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate7 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate8 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate9 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate10 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate11 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate12 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate13 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate14 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate15 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate16 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate17 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate18 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate19 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate20 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate21 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate22 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate23 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate24 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate25 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate26 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate27 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate28 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate29 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate30 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate31 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate32 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate33 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate34 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate35 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate36 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate37 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate38 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate39 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate40 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate41 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate42 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate43 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate44 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate45 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""

cqlCreate46 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate47 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""


cqlCreate48 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate49 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate50 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate51 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate52 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate53 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate54 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate55 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate56 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate57 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate58 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate59 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate60 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate61 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate62 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate63 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate64 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate65 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate66 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate67 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate68 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate69 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate70 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate71 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate72 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate73 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate74 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate75 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate76 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate77 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate78 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate79 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate80 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate81 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate82 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate83 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate84 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate85 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate86 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate87 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate88 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate89 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate90 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate91 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate92 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate93 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate94 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate95 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate96 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate97 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate98 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate99 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate100 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""


cqlCreate101 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other53:othername53{othername53:linha.othername53})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other53.geonameid = Br.geonameid
                MERGE(other53)-[r53:OTHER_NAME53]->(Br)

                return r53;"""


cqlCreate102 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other54:othername54{othername54:linha.othername54})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other54.geonameid = Br.geonameid
                MERGE(other54)-[r54:OTHER_NAME54]->(Br)

                return r54;"""


cqlCreate103 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(other55:othername55{othername55:linha.othername55})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other55.geonameid = Br.geonameid
                MERGE(other55)-[r55:OTHER_NAME55]->(Br)

                return r55;"""

cqlCreate104 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate105 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""


cqlCreate106 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate107 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate108 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate109 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate110 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate111 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate112 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate113 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate114 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate115 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate116 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate117 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate118 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate119 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate120 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate121 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate122 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate123 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate124 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate125 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate126 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate127 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate128 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate129 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate130 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate131 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate132 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate133 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate134 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate135 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate136 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate137 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate138 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate139 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate140 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate141 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate142 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate143 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate144 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate145 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate146 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate147 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate148 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate149 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate150 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate151 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate152 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate153 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate154 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate155 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate156 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate157 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate158 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""


cqlCreate159 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other53:othername53{othername53:linha.othername53})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other53.geonameid = Br.geonameid
                MERGE(other53)-[r53:OTHER_NAME53]->(Br)

                return r53;"""


cqlCreate160 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other54:othername54{othername54:linha.othername54})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other54.geonameid = Br.geonameid
                MERGE(other54)-[r54:OTHER_NAME54]->(Br)

                return r54;"""


cqlCreate161 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha


                MATCH(other55:othername55{othername55:linha.othername55})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other55.geonameid = Br.geonameid
                MERGE(other55)-[r55:OTHER_NAME55]->(Br)

                return r55;"""

cqlCreate162 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha

                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii1;"""


cqlCreate163 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate164 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate165 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate166 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate167 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate168 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate169 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate170 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate171 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate172 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate173 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate174 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate175 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate176 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate177 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate178 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate179 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate180 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate181 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate182 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate183 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate184 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate185 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate186 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate187 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate188 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate189 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate190 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate191 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate192 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate193 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate194 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate195 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate196 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate197 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate198 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate199 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate200 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate201 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate202 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate203 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate204 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate205 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate206 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate207 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate208 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate209 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate210 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate211 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate212 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate213 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate214 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate215 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate216 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""


cqlCreate217 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other53:othername53{othername53:linha.othername53})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other53.geonameid = Br.geonameid
                MERGE(other53)-[r53:OTHER_NAME53]->(Br)

                return r53;"""


cqlCreate218 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other54:othername54{othername54:linha.othername54})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other54.geonameid = Br.geonameid
                MERGE(other54)-[r54:OTHER_NAME54]->(Br)

                return r54;"""


cqlCreate219 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other55:othername55{othername55:linha.othername55})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other55.geonameid = Br.geonameid
                MERGE(other55)-[r55:OTHER_NAME55]->(Br)

                return r55;"""


cqlCreate220 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other56:othername56{othername56:linha.othername56})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other56.geonameid = Br.geonameid
                MERGE(other56)-[r56:OTHER_NAME56]->(Br)

                return r56;"""


cqlCreate221 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other57:othername57{othername57:linha.othername57})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other57.geonameid = Br.geonameid
                MERGE(other57)-[r57:OTHER_NAME57]->(Br)

                return r57;"""


cqlCreate222 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other58:othername58{othername58:linha.othername58})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other58.geonameid = Br.geonameid
                MERGE(other58)-[r58:OTHER_NAME58]->(Br)

                return r58;"""


cqlCreate223 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other59:othername59{othername59:linha.othername59})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other59.geonameid = Br.geonameid
                MERGE(other59)-[r59:OTHER_NAME59]->(Br)

                return r59;"""


cqlCreate224 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other60:othername60{othername60:linha.othername60})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other60.geonameid = Br.geonameid
                MERGE(other60)-[r60:OTHER_NAME60]->(Br)

                return r60;"""


cqlCreate225 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other61:othername61{othername61:linha.othername61})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other61.geonameid = Br.geonameid
                MERGE(other61)-[r61:OTHER_NAME61]->(Br)

                return r61;"""


cqlCreate226 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other62:othername62{othername62:linha.othername62})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other62.geonameid = Br.geonameid
                MERGE(other62)-[r62:OTHER_NAME62]->(Br)

                return r62;"""


cqlCreate227 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other63:othername63{othername63:linha.othername63})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other63.geonameid = Br.geonameid
                MERGE(other63)-[r63:OTHER_NAME63]->(Br)

                return r63;"""


cqlCreate228 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other64:othername64{othername64:linha.othername64})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other64.geonameid = Br.geonameid
                MERGE(other64)-[r64:OTHER_NAME64]->(Br)

                return r64;"""


cqlCreate229 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other65:othername65{othername65:linha.othername65})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other65.geonameid = Br.geonameid
                MERGE(other65)-[r65:OTHER_NAME65]->(Br)

                return r65;"""


cqlCreate230 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(other66:othername66{othername66:linha.othername66})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other66.geonameid = Br.geonameid
                MERGE(other66)-[r66:OTHER_NAME66]->(Br)

                return r66;"""

cqlCreate231 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate232 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate233 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate234 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate235 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate236 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate237 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate238 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate239 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate240 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate241 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate242 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate243 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate244 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate245 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate246 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate247 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate248 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate249 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate250 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate251 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate252 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate253 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate254 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate255 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate256 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate257 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate258 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate259 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate260 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate261 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate262 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate263 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate264 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate265 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate266 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate267 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate268 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate269 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate270 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate271 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate272 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate273 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate274 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate275 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate276 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate277 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate278 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate279 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate280 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate281 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate282 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate283 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate284 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate285 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""


cqlCreate286 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other53:othername53{othername53:linha.othername53})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other53.geonameid = Br.geonameid
                MERGE(other53)-[r53:OTHER_NAME53]->(Br)

                return r53;"""


cqlCreate287 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other54:othername54{othername54:linha.othername54})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other54.geonameid = Br.geonameid
                MERGE(other54)-[r54:OTHER_NAME54]->(Br)

                return r54;"""


cqlCreate288 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other55:othername55{othername55:linha.othername55})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other55.geonameid = Br.geonameid
                MERGE(other55)-[r55:OTHER_NAME55]->(Br)

                return r55;"""


cqlCreate289 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(other56:othername56{othername56:linha.othername56})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other56.geonameid = Br.geonameid
                MERGE(other56)-[r56:OTHER_NAME56]->(Br)

                return r56;"""

cqlCreate290 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate291 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate292 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate293 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate294 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate295 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate296 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate297 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate298 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate299 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate300 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate301 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate302 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate303 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate304 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate305 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate306 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate307 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate308 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate309 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate310 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate311 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate312 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate313 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate314 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate315 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate316 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate317 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate318 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate319 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate320 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate321 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate322 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate323 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate324 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate325 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate326 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate327 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate328 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate329 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate330 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate331 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate332 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate333 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate334 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate335 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate336 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate337 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate338 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate339 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate340 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate341 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate342 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate343 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate344 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""


cqlCreate345 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other53:othername53{othername53:linha.othername53})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other53.geonameid = Br.geonameid
                MERGE(other53)-[r53:OTHER_NAME53]->(Br)

                return r53;"""


cqlCreate346 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other54:othername54{othername54:linha.othername54})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other54.geonameid = Br.geonameid
                MERGE(other54)-[r54:OTHER_NAME54]->(Br)

                return r54;"""


cqlCreate347 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other55:othername55{othername55:linha.othername55})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other55.geonameid = Br.geonameid
                MERGE(other55)-[r55:OTHER_NAME55]->(Br)

                return r55;"""


cqlCreate348 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other56:othername56{othername56:linha.othername56})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other56.geonameid = Br.geonameid
                MERGE(other56)-[r56:OTHER_NAME56]->(Br)

                return r56;"""


cqlCreate349 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other57:othername57{othername57:linha.othername57})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other57.geonameid = Br.geonameid
                MERGE(other57)-[r57:OTHER_NAME57]->(Br)

                return r57;"""


cqlCreate350 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other58:othername58{othername58:linha.othername58})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other58.geonameid = Br.geonameid
                MERGE(other58)-[r58:OTHER_NAME58]->(Br)

                return r58;"""


cqlCreate351 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other59:othername59{othername59:linha.othername59})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other59.geonameid = Br.geonameid
                MERGE(other59)-[r59:OTHER_NAME59]->(Br)

                return r59;"""


cqlCreate352 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other60:othername60{othername60:linha.othername60})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other60.geonameid = Br.geonameid
                MERGE(other60)-[r60:OTHER_NAME60]->(Br)

                return r60;"""


cqlCreate353 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other61:othername61{othername61:linha.othername61})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other61.geonameid = Br.geonameid
                MERGE(other61)-[r61:OTHER_NAME61]->(Br)

                return r61;"""


cqlCreate354 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other62:othername62{othername62:linha.othername62})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other62.geonameid = Br.geonameid
                MERGE(other62)-[r62:OTHER_NAME62]->(Br)

                return r62;"""


cqlCreate355 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other63:othername63{othername63:linha.othername63})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other63.geonameid = Br.geonameid
                MERGE(other63)-[r63:OTHER_NAME63]->(Br)

                return r63;"""


cqlCreate356 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other64:othername64{othername64:linha.othername64})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other64.geonameid = Br.geonameid
                MERGE(other64)-[r64:OTHER_NAME64]->(Br)

                return r64;"""


cqlCreate357 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other65:othername65{othername65:linha.othername65})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other65.geonameid = Br.geonameid
                MERGE(other65)-[r65:OTHER_NAME65]->(Br)

                return r65;"""


cqlCreate358 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(other66:othername66{othername66:linha.othername66})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other66.geonameid = Br.geonameid
                MERGE(other66)-[r66:OTHER_NAME66]->(Br)

                return r66;"""

cqlCreate359 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate360 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate361 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate362 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate363 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate364 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate365 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate366 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate367 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate368 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate369 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate370 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate371 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate372 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate373 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate374 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate375 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate376 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate377 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate378 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate379 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate380 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate381 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate382 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate383 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate384 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate385 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate386 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate387 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate388 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate389 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate390 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate391 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate392 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate393 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate394 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate395 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate396 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate397 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate398 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate399 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate400 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate401 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate402 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate403 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate404 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate405 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate406 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate407 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate408 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate409 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate410 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate411 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate412 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate413 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""

cqlCreate414 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate415 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate416 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate417 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate418 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate419 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate420 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate421 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate422 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate423 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate424 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate425 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate426 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate427 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate428 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate429 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate430 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate431 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate432 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate433 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate434 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate435 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate436 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate437 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate438 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate439 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate440 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate441 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate442 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate443 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate444 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate445 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate446 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate447 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate448 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate449 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate450 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate451 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate452 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate453 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate454 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate455 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate456 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate457 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate458 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate459 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate460 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate461 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate462 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate463 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""

cqlCreate464 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""

cqlCreate465 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate466 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate467 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate468 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate469 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate470 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate471 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate472 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate473 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate474 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate475 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate476 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate477 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate478 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate479 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate480 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate481 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate482 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate483 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate484 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate485 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate486 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate487 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate488 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate489 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate490 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate491 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate492 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate493 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate494 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate495 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate496 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""


cqlCreate497 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other31.geonameid = Br.geonameid
                MERGE(other31)-[r31:OTHER_NAME31]->(Br)

                return r31;"""


cqlCreate498 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other32.geonameid = Br.geonameid
                MERGE(other32)-[r32:OTHER_NAME32]->(Br)

                return r32;"""


cqlCreate499 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other33.geonameid = Br.geonameid
                MERGE(other33)-[r33:OTHER_NAME33]->(Br)

                return r33;"""


cqlCreate500 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other34.geonameid = Br.geonameid
                MERGE(other34)-[r34:OTHER_NAME34]->(Br)

                return r34;"""


cqlCreate501 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other35.geonameid = Br.geonameid
                MERGE(other35)-[r35:OTHER_NAME35]->(Br)

                return r35;"""


cqlCreate502 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other36.geonameid = Br.geonameid
                MERGE(other36)-[r36:OTHER_NAME36]->(Br)

                return r36;"""


cqlCreate503 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other37.geonameid = Br.geonameid
                MERGE(other37)-[r37:OTHER_NAME37]->(Br)

                return r37;"""


cqlCreate504 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other38.geonameid = Br.geonameid
                MERGE(other38)-[r38:OTHER_NAME38]->(Br)

                return r38;"""


cqlCreate505 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other39.geonameid = Br.geonameid
                MERGE(other39)-[r39:OTHER_NAME39]->(Br)

                return r39;"""


cqlCreate506 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other40.geonameid = Br.geonameid
                MERGE(other40)-[r40:OTHER_NAME40]->(Br)

                return r40;"""


cqlCreate507 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other41.geonameid = Br.geonameid
                MERGE(other41)-[r41:OTHER_NAME41]->(Br)

                return r41;"""


cqlCreate508 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other42.geonameid = Br.geonameid
                MERGE(other42)-[r42:OTHER_NAME42]->(Br)

                return r42;"""


cqlCreate509 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other43.geonameid = Br.geonameid
                MERGE(other43)-[r43:OTHER_NAME43]->(Br)

                return r43;"""


cqlCreate510 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other44.geonameid = Br.geonameid
                MERGE(other44)-[r44:OTHER_NAME44]->(Br)

                return r44;"""


cqlCreate511 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other45.geonameid = Br.geonameid
                MERGE(other45)-[r45:OTHER_NAME45]->(Br)

                return r45;"""


cqlCreate512 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other46.geonameid = Br.geonameid
                MERGE(other46)-[r46:OTHER_NAME46]->(Br)

                return r46;"""


cqlCreate513 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other47.geonameid = Br.geonameid
                MERGE(other47)-[r47:OTHER_NAME47]->(Br)

                return r47;"""


cqlCreate514 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other48.geonameid = Br.geonameid
                MERGE(other48)-[r48:OTHER_NAME48]->(Br)

                return r48;"""


cqlCreate515 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other49.geonameid = Br.geonameid
                MERGE(other49)-[r49:OTHER_NAME49]->(Br)

                return r49;"""


cqlCreate516 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other50.geonameid = Br.geonameid
                MERGE(other50)-[r50:OTHER_NAME50]->(Br)

                return r50;"""


cqlCreate517 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other51:othername51{othername51:linha.othername51})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other51.geonameid = Br.geonameid
                MERGE(other51)-[r51:OTHER_NAME51]->(Br)

                return r51;"""


cqlCreate518 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other52:othername52{othername52:linha.othername52})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other52.geonameid = Br.geonameid
                MERGE(other52)-[r52:OTHER_NAME52]->(Br)

                return r52;"""


cqlCreate519 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other53:othername53{othername53:linha.othername53})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other53.geonameid = Br.geonameid
                MERGE(other53)-[r53:OTHER_NAME53]->(Br)

                return r53;"""


cqlCreate520 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other54:othername54{othername54:linha.othername54})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other54.geonameid = Br.geonameid
                MERGE(other54)-[r54:OTHER_NAME54]->(Br)

                return r54;"""


cqlCreate521 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other55:othername55{othername55:linha.othername55})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other55.geonameid = Br.geonameid
                MERGE(other55)-[r55:OTHER_NAME55]->(Br)

                return r55;"""


cqlCreate522 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other56:othername56{othername56:linha.othername56})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other56.geonameid = Br.geonameid
                MERGE(other56)-[r56:OTHER_NAME56]->(Br)

                return r56;"""


cqlCreate523 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other57:othername57{othername57:linha.othername57})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other57.geonameid = Br.geonameid
                MERGE(other57)-[r57:OTHER_NAME57]->(Br)

                return r57;"""


cqlCreate524 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other58:othername58{othername58:linha.othername58})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other58.geonameid = Br.geonameid
                MERGE(other58)-[r58:OTHER_NAME58]->(Br)

                return r58;"""


cqlCreate525 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other59:othername59{othername59:linha.othername59})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other59.geonameid = Br.geonameid
                MERGE(other59)-[r59:OTHER_NAME59]->(Br)

                return r59;"""


cqlCreate526 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other60:othername60{othername60:linha.othername60})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other60.geonameid = Br.geonameid
                MERGE(other60)-[r60:OTHER_NAME60]->(Br)

                return r60;"""


cqlCreate527 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other61:othername61{othername61:linha.othername61})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other61.geonameid = Br.geonameid
                MERGE(other61)-[r61:OTHER_NAME61]->(Br)

                return r61;"""


cqlCreate528 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other62:othername62{othername62:linha.othername62})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other62.geonameid = Br.geonameid
                MERGE(other62)-[r62:OTHER_NAME62]->(Br)

                return r62;"""


cqlCreate529 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other63:othername63{othername63:linha.othername63})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other63.geonameid = Br.geonameid
                MERGE(other63)-[r63:OTHER_NAME63]->(Br)

                return r63;"""


cqlCreate530 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other64:othername64{othername64:linha.othername64})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other64.geonameid = Br.geonameid
                MERGE(other64)-[r64:OTHER_NAME64]->(Br)

                return r64;"""


cqlCreate531 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other65:othername65{othername65:linha.othername65})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other65.geonameid = Br.geonameid
                MERGE(other65)-[r65:OTHER_NAME65]->(Br)

                return r65;"""


cqlCreate532 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(other66:othername66{othername66:linha.othername66})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other66.geonameid = Br.geonameid
                MERGE(other66)-[r66:OTHER_NAME66]->(Br)

                return r66;"""

cqlCreate533 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate534 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate535 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate536 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate537 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate538 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate539 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate540 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate541 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate542 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate543 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate544 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate545 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate546 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""

cqlCreate547 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""


cqlCreate548 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate549 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate550 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate551 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate552 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate553 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate554 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate555 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate556 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate557 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate558 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate559 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""


cqlCreate560 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other11.geonameid = Br.geonameid
                MERGE(other11)-[r11:OTHER_NAME11]->(Br)

                return r11;"""


cqlCreate561 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other12.geonameid = Br.geonameid
                MERGE(other12)-[r12:OTHER_NAME12]->(Br)

                return r12;"""


cqlCreate562 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other13.geonameid = Br.geonameid
                MERGE(other13)-[r13:OTHER_NAME13]->(Br)

                return r13;"""


cqlCreate563 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other14.geonameid = Br.geonameid
                MERGE(other14)-[r14:OTHER_NAME14]->(Br)

                return r14;"""


cqlCreate564 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other15.geonameid = Br.geonameid
                MERGE(other15)-[r15:OTHER_NAME15]->(Br)

                return r15;"""


cqlCreate565 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other16.geonameid = Br.geonameid
                MERGE(other16)-[r16:OTHER_NAME16]->(Br)

                return r16;"""


cqlCreate566 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other17.geonameid = Br.geonameid
                MERGE(other17)-[r17:OTHER_NAME17]->(Br)

                return r17;"""


cqlCreate567 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other18.geonameid = Br.geonameid
                MERGE(other18)-[r18:OTHER_NAME18]->(Br)

                return r18;"""


cqlCreate568 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other19.geonameid = Br.geonameid
                MERGE(other19)-[r19:OTHER_NAME19]->(Br)

                return r19;"""


cqlCreate569 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other20.geonameid = Br.geonameid
                MERGE(other20)-[r20:OTHER_NAME20]->(Br)

                return r20;"""


cqlCreate570 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other21.geonameid = Br.geonameid
                MERGE(other21)-[r21:OTHER_NAME21]->(Br)

                return r21;"""


cqlCreate571 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other22.geonameid = Br.geonameid
                MERGE(other22)-[r22:OTHER_NAME22]->(Br)

                return r22;"""


cqlCreate572 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other23.geonameid = Br.geonameid
                MERGE(other23)-[r23:OTHER_NAME23]->(Br)

                return r23;"""


cqlCreate573 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other24.geonameid = Br.geonameid
                MERGE(other24)-[r24:OTHER_NAME24]->(Br)

                return r24;"""


cqlCreate574 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other25.geonameid = Br.geonameid
                MERGE(other25)-[r25:OTHER_NAME25]->(Br)

                return r25;"""


cqlCreate575 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other26.geonameid = Br.geonameid
                MERGE(other26)-[r26:OTHER_NAME26]->(Br)

                return r26;"""


cqlCreate576 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other27.geonameid = Br.geonameid
                MERGE(other27)-[r27:OTHER_NAME27]->(Br)

                return r27;"""


cqlCreate577 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other28.geonameid = Br.geonameid
                MERGE(other28)-[r28:OTHER_NAME28]->(Br)

                return r28;"""


cqlCreate578 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other29.geonameid = Br.geonameid
                MERGE(other29)-[r29:OTHER_NAME29]->(Br)

                return r29;"""


cqlCreate579 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other30.geonameid = Br.geonameid
                MERGE(other30)-[r30:OTHER_NAME30]->(Br)

                return r30;"""

cqlCreate580 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""

cqlCreate581 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate582 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate583 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate584 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate585 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate586 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate587 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate588 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate589 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""


cqlCreate590 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other8.geonameid = Br.geonameid
                MERGE(other8)-[r8:OTHER_NAME8]->(Br)

                return r8;"""


cqlCreate591 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other9.geonameid = Br.geonameid
                MERGE(other9)-[r9:OTHER_NAME9]->(Br)

                return r9;"""


cqlCreate592 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other10.geonameid = Br.geonameid
                MERGE(other10)-[r10:OTHER_NAME10]->(Br)

                return r10;"""

cqlCreate593 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""

cqlCreate594 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha

                CREATE (Br:LOCATIONS {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,    
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,  
                countrycode:linha.countrycode, admin4code:linha.admin4code, 
                modificationdate:linha.modificationdate, longitude:linha.longitude})
                
                WITH linha WHERE NOT linha.asciiname IS null
                CREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername0 IS null
                CREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername1 IS null
                CREATE (other1:othername1{othername1:linha.othername1, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername2 IS null
                CREATE (other2:othername2{othername2:linha.othername2, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername3 IS null
                CREATE (other3:othername3{othername3:linha.othername3, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername4 IS null
                CREATE (other4:othername4{othername4:linha.othername4, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername5 IS null
                CREATE (other5:othername5{othername5:linha.othername5, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername6 IS null
                CREATE (other6:othername6{othername6:linha.othername6, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername7 IS null
                CREATE (other7:othername7{othername7:linha.othername7, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername8 IS null
                CREATE (other8:othername8{othername8:linha.othername8, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername9 IS null
                CREATE (other9:othername9{othername9:linha.othername9, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername10 IS null
                CREATE (other10:othername10{othername10:linha.othername10, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername11 IS null
                CREATE (other11:othername11{othername11:linha.othername11, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername12 IS null
                CREATE (other12:othername12{othername12:linha.othername12, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername13 IS null
                CREATE (other13:othername13{othername13:linha.othername13, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername14 IS null
                CREATE (other14:othername14{othername14:linha.othername14, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername15 IS null
                CREATE (other15:othername15{othername15:linha.othername15, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername16 IS null
                CREATE (other16:othername16{othername16:linha.othername16, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername17 IS null
                CREATE (other17:othername17{othername17:linha.othername17, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername18 IS null
                CREATE (other18:othername18{othername18:linha.othername18, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername19 IS null
                CREATE (other19:othername19{othername19:linha.othername19, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername20 IS null
                CREATE (other20:othername20{othername20:linha.othername20, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername21 IS null
                CREATE (other21:othername21{othername21:linha.othername21, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername22 IS null
                CREATE (other22:othername22{othername22:linha.othername22, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername23 IS null
                CREATE (other23:othername23{othername23:linha.othername23, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername24 IS null
                CREATE (other24:othername24{othername24:linha.othername24, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername25 IS null
                CREATE (other25:othername25{othername25:linha.othername25, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername26 IS null
                CREATE (other26:othername26{othername26:linha.othername26, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername27 IS null
                CREATE (other27:othername27{othername27:linha.othername27, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername28 IS null
                CREATE (other28:othername28{othername28:linha.othername28, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername29 IS null
                CREATE (other29:othername29{othername29:linha.othername29, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername30 IS null
                CREATE (other30:othername30{othername30:linha.othername30, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername31 IS null
                CREATE (other31:othername31{othername31:linha.othername31, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername32 IS null
                CREATE (other32:othername32{othername32:linha.othername32, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername33 IS null
                CREATE (other33:othername33{othername33:linha.othername33, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername34 IS null
                CREATE (other34:othername34{othername34:linha.othername34, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername35 IS null
                CREATE (other35:othername35{othername35:linha.othername35, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername36 IS null
                CREATE (other36:othername36{othername36:linha.othername36, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername37 IS null
                CREATE (other37:othername37{othername37:linha.othername37, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername38 IS null
                CREATE (other38:othername38{othername38:linha.othername38, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername39 IS null
                CREATE (other39:othername39{othername39:linha.othername39, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername40 IS null
                CREATE (other40:othername40{othername40:linha.othername40, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other41:othername41{othername41:linha.othername41, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108, geonameid:linha.geonameid})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109, geonameid:linha.geonameid})"""

cqlCreate595 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other0.geonameid = Br.geonameid
                MERGE(other0)-[r0:OTHER_NAME0]->(Br)

                return r0;"""


cqlCreate596 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other1.geonameid = Br.geonameid
                MERGE(other1)-[r1:OTHER_NAME1]->(Br)

                return r1;"""


cqlCreate597 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other2.geonameid = Br.geonameid
                MERGE(other2)-[r2:OTHER_NAME2]->(Br)

                return r2;"""


cqlCreate598 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other3.geonameid = Br.geonameid
                MERGE(other3)-[r3:OTHER_NAME3]->(Br)

                return r3;"""


cqlCreate599 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other4.geonameid = Br.geonameid
                MERGE(other4)-[r4:OTHER_NAME4]->(Br)

                return r4;"""


cqlCreate600 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other5.geonameid = Br.geonameid
                MERGE(other5)-[r5:OTHER_NAME5]->(Br)

                return r5;"""


cqlCreate601 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other6.geonameid = Br.geonameid
                MERGE(other6)-[r6:OTHER_NAME6]->(Br)

                return r6;"""


cqlCreate602 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE other7.geonameid = Br.geonameid
                MERGE(other7)-[r7:OTHER_NAME7]->(Br)

                return r7;"""

cqlCreate603 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha


                MATCH(ascii:ASCIINAME{asciiname:linha.asciiname})
                MATCH(Br:LOCATIONS{name:linha.name})
                WHERE ascii.geonameid = Br.geonameid
                MERGE(ascii)-[ascii1:ASCIINAME]->(Br)

                return ascii;"""

cqlCreate604 = """LOAD CSV WITH HEADERS FROM 'file:///country.csv' AS linha
                CREATE (country:BRAZIL{name:linha.name}) RETURN country"""

cqlCreate605 = """LOAD CSV WITH HEADERS FROM 'file:///states_district.csv' AS linha
                CREATE (states:STATES{name:linha.name}) RETURN states"""

cqlCreate606 = """LOAD CSV WITH HEADERS FROM 'file:///regions.csv' AS linha
                CREATE (regions:REGIONS{name:linha.name}) RETURN regions"""

cqlCreate607 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_0.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate608 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_1.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate609 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_2.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate610 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_3.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate611 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_4.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate612 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_5.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate613 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_6.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate614 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_7.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate615 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_8.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate616 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_9.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate617 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_10.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate618 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_11.csv' AS linha
                MATCH(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""

cqlCreate619 = """LOAD CSV WITH HEADERS FROM 'file:///OtherNames_12.csv' AS linha
                MERGE(location:LOCATIONS), (country:BRAZIL)
                WHERE location.name = linha.name AND country.name = "Brasil"

                MERGE (location)-[isin:IS_IN]->(country)

                return isin;"""


# Crete indexes:
cqlCreate00 = """create index other0_index for (o0:othername0) on (o0.othername0);"""
cqlCreate01 = """create index other1_index for (o1:othername1) on (o1.othername1);"""
cqlCreate02 = """create index other2_index for (o2:othername2) on (o2.othername2);"""
cqlCreate03 = """create index other3_index for (o3:othername3) on (o3.othername3);"""
cqlCreate04 = """create index other4_index for (o4:othername4) on (o4.othername4);"""
cqlCreate05 = """create index other5_index for (o5:othername5) on (o5.othername5);"""
cqlCreate06 = """create index other6_index for (o6:othername6) on (o6.othername6);"""
cqlCreate07 = """create index other7_index for (o7:othername7) on (o7.othername7);"""
cqlCreate08 = """create index other8_index for (o8:othername8) on (o8.othername8);"""
cqlCreate09 = """create index other9_index for (o9:othername9) on (o9.othername9);"""
cqlCreate010 = """create index other10_index for (o10:othername10) on (o10.othername10);"""
cqlCreate011 = """create index other11_index for (o11:othername11) on (o11.othername11);"""
cqlCreate012 = """create index other12_index for (o12:othername12) on (o12.othername12);"""
cqlCreate013 = """create index other13_index for (o13:othername13) on (o13.othername13);"""
cqlCreate014 = """create index other14_index for (o14:othername14) on (o14.othername14);"""
cqlCreate015 = """create index other15_index for (o15:othername15) on (o15.othername15);"""
cqlCreate016 = """create index other16_index for (o16:othername16) on (o16.othername16);"""
cqlCreate017 = """create index other17_index for (o17:othername17) on (o17.othername17);"""
cqlCreate018 = """create index other18_index for (o18:othername18) on (o18.othername18);"""
cqlCreate019 = """create index other19_index for (o19:othername19) on (o19.othername19);"""
cqlCreate020 = """create index other20_index for (o20:othername20) on (o20.othername20);"""
cqlCreate021 = """create index other21_index for (o21:othername21) on (o21.othername21);"""
cqlCreate022 = """create index other22_index for (o22:othername22) on (o22.othername22);"""
cqlCreate023 = """create index other23_index for (o23:othername23) on (o23.othername23);"""
cqlCreate024 = """create index other24_index for (o24:othername24) on (o24.othername24);"""
cqlCreate025 = """create index other25_index for (o25:othername25) on (o25.othername25);"""
cqlCreate026 = """create index other26_index for (o26:othername26) on (o26.othername26);"""
cqlCreate027 = """create index other27_index for (o27:othername27) on (o27.othername27);"""
cqlCreate028 = """create index other28_index for (o28:othername28) on (o28.othername28);"""
cqlCreate029 = """create index other29_index for (o29:othername29) on (o29.othername29);"""
cqlCreate030 = """create index other30_index for (o30:othername30) on (o30.othername30);"""
cqlCreate031 = """create index other31_index for (o31:othername31) on (o31.othername31);"""
cqlCreate032 = """create index other32_index for (o32:othername32) on (o32.othername32);"""
cqlCreate033 = """create index other33_index for (o33:othername33) on (o33.othername33);"""
cqlCreate034 = """create index other34_index for (o34:othername34) on (o34.othername34);"""
cqlCreate035 = """create index other35_index for (o35:othername35) on (o35.othername35);"""
cqlCreate036 = """create index other36_index for (o36:othername36) on (o36.othername36);"""
cqlCreate037 = """create index other37_index for (o37:othername37) on (o37.othername37);"""
cqlCreate038 = """create index other38_index for (o38:othername38) on (o38.othername38);"""
cqlCreate039 = """create index other39_index for (o39:othername39) on (o39.othername39);"""
cqlCreate040 = """create index other40_index for (o40:othername40) on (o40.othername40);"""
cqlCreate041 = """create index other41_index for (o41:othername41) on (o41.othername41);"""
cqlCreate042 = """create index other42_index for (o42:othername42) on (o42.othername42);"""
cqlCreate043 = """create index other43_index for (o43:othername43) on (o43.othername43);"""
cqlCreate044 = """create index other44_index for (o44:othername44) on (o44.othername44);"""
cqlCreate045 = """create index other45_index for (o45:othername45) on (o45.othername45);"""
cqlCreate046 = """create index other46_index for (o46:othername46) on (o46.othername46);"""
cqlCreate047 = """create index other47_index for (o47:othername47) on (o47.othername47);"""
cqlCreate048 = """create index other48_index for (o48:othername48) on (o48.othername48);"""
cqlCreate049 = """create index other49_index for (o49:othername49) on (o49.othername49);"""
cqlCreate050 = """create index other50_index for (o50:othername50) on (o50.othername50);"""
cqlCreate051 = """create index other51_index for (o51:othername51) on (o51.othername51);"""
cqlCreate052 = """create index other52_index for (o52:othername52) on (o52.othername52);"""
cqlCreate053 = """create index other53_index for (o53:othername53) on (o53.othername53);"""
cqlCreate054 = """create index other54_index for (o54:othername54) on (o54.othername54);"""
cqlCreate055 = """create index other55_index for (o55:othername55) on (o55.othername55);"""
cqlCreate056 = """create index other56_index for (o56:othername56) on (o56.othername56);"""
cqlCreate057 = """create index other57_index for (o57:othername57) on (o57.othername57);"""
cqlCreate058 = """create index other58_index for (o58:othername58) on (o58.othername58);"""
cqlCreate059 = """create index other59_index for (o59:othername59) on (o59.othername59);"""
cqlCreate060 = """create index other60_index for (o60:othername60) on (o60.othername60);"""
cqlCreate061 = """create index other61_index for (o61:othername61) on (o61.othername61);"""
cqlCreate062 = """create index other62_index for (o62:othername62) on (o62.othername62);"""
cqlCreate063 = """create index other63_index for (o63:othername63) on (o63.othername63);"""
cqlCreate064 = """create index other64_index for (o64:othername64) on (o64.othername64);"""
cqlCreate065 = """create index other65_index for (o65:othername65) on (o65.othername65);"""
cqlCreate066 = """create index other66_index for (o66:othername66) on (o66.othername66);"""
cqlCreate067 = """create index ascii_index for (ascii:ASCIINAME) on (ascii.asciiname);"""
cqlCreate068 = """create index name_index for (br:LOCATIONS) on (br.name);"""
cqlCreate069 = """create index country_index for (country:BRAZIL) on (country.name);"""
cqlCreate070 = """create index region_index for (region:REGIONS) on (region.name);"""
cqlCreate071 = """create index states_index for (states:STATES) on (states.name);"""


# Function to create a csv file with the alternative names separated by columns:
def div_names():
    df = pd.read_csv('BR (1).csv')
    df = df.join(df['alternatenames'].str.split(
        '$', expand=True).add_prefix('othername'))
    print(df)

    remove = ['alternatenames', 'othername166', 'othername67', 'othername165', 'othername164', 'othername164', 'othername163',
              'othername162', 'othername161', 'othername160', 'othername159', 'othername158', 'othername157', 'othername156', 'othername155',
              'othername154', 'othername153', 'othername152', 'othername151', 'othername150', 'othername149', 'othername148', 'othername147',
              'othername146', 'othername145', 'othername144', 'othername145', 'othername144', 'othername143', 'othername142', 'othername141',
              'othername140', 'othername139', 'othername138', 'othername137', 'othername136', 'othername135', 'othername134', 'othername133',
              'othername132', 'othername131', 'othername130', 'othername129', 'othername128', 'othername127', 'othername126', 'othername125',
              'othername124', 'othername123', 'othername122', 'othername121', 'othername120', 'othername119', 'othername118', 'othername117',
              'othername116', 'othername115', 'othername114', 'othername113', 'othername112', 'othername111', 'othername110', 'othername109',
              'othername108', 'othername107', 'othername106', 'othername105', 'othername104', 'othername103', 'othername102', 'othername101',
              'othername100', 'othername99', 'othername98', 'othername97', 'othername96', 'othername95', 'othername94', 'othername93', 'othername92',
              'othername91', 'othername90', 'othername89', 'othername88', 'othername87', 'othername86', 'othername85', 'othername84', 'othername83',
              'othername82', 'othername81', 'othername80', 'othername79', 'othername78', 'othername77', 'othername76', 'othername75', 'othername74',
              'othername73', 'othername72', 'othername71', 'othername70', 'othername69', 'othername68', 'othername67']

    df2 = df.drop(remove, axis=1)
    df2.to_csv('OtherNames.csv')
#div_names()


# Function to create a relationship between the locations of the OtherNames_0 file and the LOCATIONS node.
def create_relatBR_0():
    # Read CSV data
    df = pd.read_csv("OtherNames_0.csv")
# Read WKT data from file
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wktfile:
        wkt_data = shapely.wkt.loads(wktfile.read())
# Check the coordinates between the CSV and WKT data
        for i, row in df.iterrows():
            csv_coord = (float(row[5]), float(row[4]))
            if wkt_data.contains(shapely.geometry.Point(*csv_coord)):
                with db.session() as session:
                    session.run("MATCH (country:BRAZIL {name: 'Brasil'}), (location:LOCATIONS {longitude: $longitude, latitude: $latitude}) "
                                "MERGE (location)-[:IS_IN]->(country)",
                                longitude=row[5], latitude=row[4])
                    print("created\n", ":", csv_coord)
            else:
                print("The following coordinates do not match",
                      i+1, ":", csv_coord)
#create_relatBR_0()


def create_relatBR_1():
    # Read CSV data
    df = pd.read_csv("OtherNames_1.csv")
# Read WKT data from file
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wktfile:
        wkt_data = shapely.wkt.loads(wktfile.read())
# Check the coordinates between the CSV and WKT data
        for i, row in df.iterrows():
            csv_coord = (float(row[5]), float(row[4]))
            if wkt_data.contains(shapely.geometry.Point(*csv_coord)):
                with db.session() as graphDB_Session:
                    graphDB_Session.run(cqlCreate608)
                    print("created\n")
            else:

                print("The following coordinates do not match",
                      i+1, ":", csv_coord)
#create_relatBR_1()


# Create main nodes:
def create_nodes():
    with db.session() as graphDB_Session:
        graphDB_Session.run(cqlCreate0)
        graphDB_Session.run(cqlCreate47)
        graphDB_Session.run(cqlCreate105)
        graphDB_Session.run(cqlCreate163)
        graphDB_Session.run(cqlCreate232)
        graphDB_Session.run(cqlCreate291)
        graphDB_Session.run(cqlCreate360)
        graphDB_Session.run(cqlCreate415)
        graphDB_Session.run(cqlCreate465)
        graphDB_Session.run(cqlCreate534)
        graphDB_Session.run(cqlCreate548)
        graphDB_Session.run(cqlCreate581)
        graphDB_Session.run(cqlCreate594)
        graphDB_Session.run(cqlCreate604)
        graphDB_Session.run(cqlCreate605)
        graphDB_Session.run(cqlCreate606)
create_nodes()

# Create main indexes
def create_indexes():
    with db.session() as graphDB_Session:
        graphDB_Session.run(cqlCreate00)
        graphDB_Session.run(cqlCreate01)
        graphDB_Session.run(cqlCreate02)
        graphDB_Session.run(cqlCreate03)
        graphDB_Session.run(cqlCreate04)
        graphDB_Session.run(cqlCreate05)
        graphDB_Session.run(cqlCreate06)
        graphDB_Session.run(cqlCreate07)
        graphDB_Session.run(cqlCreate08)
        graphDB_Session.run(cqlCreate09)
        graphDB_Session.run(cqlCreate010)
        graphDB_Session.run(cqlCreate011)
        graphDB_Session.run(cqlCreate012)
        graphDB_Session.run(cqlCreate013)
        graphDB_Session.run(cqlCreate014)
        graphDB_Session.run(cqlCreate015)
        graphDB_Session.run(cqlCreate016)
        graphDB_Session.run(cqlCreate017)
        graphDB_Session.run(cqlCreate018)
        graphDB_Session.run(cqlCreate019)
        graphDB_Session.run(cqlCreate020)
        graphDB_Session.run(cqlCreate021)
        graphDB_Session.run(cqlCreate022)
        graphDB_Session.run(cqlCreate023)
        graphDB_Session.run(cqlCreate024)
        graphDB_Session.run(cqlCreate025)
        graphDB_Session.run(cqlCreate026)
        graphDB_Session.run(cqlCreate027)
        graphDB_Session.run(cqlCreate028)
        graphDB_Session.run(cqlCreate029)
        graphDB_Session.run(cqlCreate030)
        graphDB_Session.run(cqlCreate031)
        graphDB_Session.run(cqlCreate032)
        graphDB_Session.run(cqlCreate033)
        graphDB_Session.run(cqlCreate034)
        graphDB_Session.run(cqlCreate035)
        graphDB_Session.run(cqlCreate036)
        graphDB_Session.run(cqlCreate037)
        graphDB_Session.run(cqlCreate038)
        graphDB_Session.run(cqlCreate039)
        graphDB_Session.run(cqlCreate040)
        graphDB_Session.run(cqlCreate041)
        graphDB_Session.run(cqlCreate042)
        graphDB_Session.run(cqlCreate043)
        graphDB_Session.run(cqlCreate044)
        graphDB_Session.run(cqlCreate045)
        graphDB_Session.run(cqlCreate046)
        graphDB_Session.run(cqlCreate047)
        graphDB_Session.run(cqlCreate048)
        graphDB_Session.run(cqlCreate049)
        graphDB_Session.run(cqlCreate050)
        graphDB_Session.run(cqlCreate051)
        graphDB_Session.run(cqlCreate052)
        graphDB_Session.run(cqlCreate053)
        graphDB_Session.run(cqlCreate054)
        graphDB_Session.run(cqlCreate055)
        graphDB_Session.run(cqlCreate056)
        graphDB_Session.run(cqlCreate057)
        graphDB_Session.run(cqlCreate058)
        graphDB_Session.run(cqlCreate059)
        graphDB_Session.run(cqlCreate060)
        graphDB_Session.run(cqlCreate061)
        graphDB_Session.run(cqlCreate062)
        graphDB_Session.run(cqlCreate063)
        graphDB_Session.run(cqlCreate064)
        graphDB_Session.run(cqlCreate065)
        graphDB_Session.run(cqlCreate066)
        graphDB_Session.run(cqlCreate067)
        graphDB_Session.run(cqlCreate068)
        graphDB_Session.run(cqlCreate069)
        graphDB_Session.run(cqlCreate070)
        graphDB_Session.run(cqlCreate071)
#create_indexes()


# Create main realtionships
def create_relationships():
    with db.session() as graphDB_Session:
        graphDB_Session.run(cqlCreate1)
        graphDB_Session.run(cqlCreate2)
        graphDB_Session.run(cqlCreate3)
        graphDB_Session.run(cqlCreate4)
        graphDB_Session.run(cqlCreate5)
        graphDB_Session.run(cqlCreate6)
        graphDB_Session.run(cqlCreate7)
        graphDB_Session.run(cqlCreate8)
        graphDB_Session.run(cqlCreate9)
        graphDB_Session.run(cqlCreate10)
        graphDB_Session.run(cqlCreate11)
        graphDB_Session.run(cqlCreate12)
        graphDB_Session.run(cqlCreate13)
        graphDB_Session.run(cqlCreate14)
        graphDB_Session.run(cqlCreate15)
        graphDB_Session.run(cqlCreate16)
        graphDB_Session.run(cqlCreate17)
        graphDB_Session.run(cqlCreate18)
        graphDB_Session.run(cqlCreate19)
        graphDB_Session.run(cqlCreate20)
        graphDB_Session.run(cqlCreate21)
        graphDB_Session.run(cqlCreate22)
        graphDB_Session.run(cqlCreate23)
        graphDB_Session.run(cqlCreate24)
        graphDB_Session.run(cqlCreate25)
        graphDB_Session.run(cqlCreate26)
        graphDB_Session.run(cqlCreate27)
        graphDB_Session.run(cqlCreate28)
        graphDB_Session.run(cqlCreate29)
        graphDB_Session.run(cqlCreate30)
        graphDB_Session.run(cqlCreate31)
        graphDB_Session.run(cqlCreate32)
        graphDB_Session.run(cqlCreate33)
        graphDB_Session.run(cqlCreate34)
        graphDB_Session.run(cqlCreate35)
        graphDB_Session.run(cqlCreate36)
        graphDB_Session.run(cqlCreate37)
        graphDB_Session.run(cqlCreate38)
        graphDB_Session.run(cqlCreate39)
        graphDB_Session.run(cqlCreate40)
        graphDB_Session.run(cqlCreate41)
        graphDB_Session.run(cqlCreate42)
        graphDB_Session.run(cqlCreate43)
        graphDB_Session.run(cqlCreate44)
        graphDB_Session.run(cqlCreate45)
        graphDB_Session.run(cqlCreate46)
        graphDB_Session.run(cqlCreate48)
        graphDB_Session.run(cqlCreate49)
        graphDB_Session.run(cqlCreate50)
        graphDB_Session.run(cqlCreate51)
        graphDB_Session.run(cqlCreate52)
        graphDB_Session.run(cqlCreate53)
        graphDB_Session.run(cqlCreate54)
        graphDB_Session.run(cqlCreate55)
        graphDB_Session.run(cqlCreate56)
        graphDB_Session.run(cqlCreate57)
        graphDB_Session.run(cqlCreate58)
        graphDB_Session.run(cqlCreate59)
        graphDB_Session.run(cqlCreate60)
        graphDB_Session.run(cqlCreate61)
        graphDB_Session.run(cqlCreate62)
        graphDB_Session.run(cqlCreate63)
        graphDB_Session.run(cqlCreate64)
        graphDB_Session.run(cqlCreate65)
        graphDB_Session.run(cqlCreate66)
        graphDB_Session.run(cqlCreate67)
        graphDB_Session.run(cqlCreate68)
        graphDB_Session.run(cqlCreate69)
        graphDB_Session.run(cqlCreate70)
        graphDB_Session.run(cqlCreate71)
        graphDB_Session.run(cqlCreate72)
        graphDB_Session.run(cqlCreate73)
        graphDB_Session.run(cqlCreate74)
        graphDB_Session.run(cqlCreate75)
        graphDB_Session.run(cqlCreate76)
        graphDB_Session.run(cqlCreate77)
        graphDB_Session.run(cqlCreate78)
        graphDB_Session.run(cqlCreate79)
        graphDB_Session.run(cqlCreate80)
        graphDB_Session.run(cqlCreate81)
        graphDB_Session.run(cqlCreate82)
        graphDB_Session.run(cqlCreate83)
        graphDB_Session.run(cqlCreate84)
        graphDB_Session.run(cqlCreate85)
        graphDB_Session.run(cqlCreate86)
        graphDB_Session.run(cqlCreate87)
        graphDB_Session.run(cqlCreate88)
        graphDB_Session.run(cqlCreate89)
        graphDB_Session.run(cqlCreate90)
        graphDB_Session.run(cqlCreate91)
        graphDB_Session.run(cqlCreate92)
        graphDB_Session.run(cqlCreate93)
        graphDB_Session.run(cqlCreate94)
        graphDB_Session.run(cqlCreate95)
        graphDB_Session.run(cqlCreate96)
        graphDB_Session.run(cqlCreate97)
        graphDB_Session.run(cqlCreate98)
        graphDB_Session.run(cqlCreate99)
        graphDB_Session.run(cqlCreate100)
        graphDB_Session.run(cqlCreate101)
        graphDB_Session.run(cqlCreate102)
        graphDB_Session.run(cqlCreate103)
        graphDB_Session.run(cqlCreate104)
        graphDB_Session.run(cqlCreate106)
        graphDB_Session.run(cqlCreate107)
        graphDB_Session.run(cqlCreate108)
        graphDB_Session.run(cqlCreate109)
        graphDB_Session.run(cqlCreate110)
        graphDB_Session.run(cqlCreate111)
        graphDB_Session.run(cqlCreate112)
        graphDB_Session.run(cqlCreate113)
        graphDB_Session.run(cqlCreate114)
        graphDB_Session.run(cqlCreate115)
        graphDB_Session.run(cqlCreate116)
        graphDB_Session.run(cqlCreate117)
        graphDB_Session.run(cqlCreate118)
        graphDB_Session.run(cqlCreate119)
        graphDB_Session.run(cqlCreate120)
        graphDB_Session.run(cqlCreate121)
        graphDB_Session.run(cqlCreate122)
        graphDB_Session.run(cqlCreate123)
        graphDB_Session.run(cqlCreate124)
        graphDB_Session.run(cqlCreate125)
        graphDB_Session.run(cqlCreate126)
        graphDB_Session.run(cqlCreate127)
        graphDB_Session.run(cqlCreate128)
        graphDB_Session.run(cqlCreate129)
        graphDB_Session.run(cqlCreate130)
        graphDB_Session.run(cqlCreate131)
        graphDB_Session.run(cqlCreate132)
        graphDB_Session.run(cqlCreate133)
        graphDB_Session.run(cqlCreate134)
        graphDB_Session.run(cqlCreate135)
        graphDB_Session.run(cqlCreate136)
        graphDB_Session.run(cqlCreate137)
        graphDB_Session.run(cqlCreate138)
        graphDB_Session.run(cqlCreate139)
        graphDB_Session.run(cqlCreate140)
        graphDB_Session.run(cqlCreate141)
        graphDB_Session.run(cqlCreate142)
        graphDB_Session.run(cqlCreate143)
        graphDB_Session.run(cqlCreate144)
        graphDB_Session.run(cqlCreate145)
        graphDB_Session.run(cqlCreate146)
        graphDB_Session.run(cqlCreate147)
        graphDB_Session.run(cqlCreate148)
        graphDB_Session.run(cqlCreate149)
        graphDB_Session.run(cqlCreate150)
        graphDB_Session.run(cqlCreate151)
        graphDB_Session.run(cqlCreate152)
        graphDB_Session.run(cqlCreate153)
        graphDB_Session.run(cqlCreate154)
        graphDB_Session.run(cqlCreate155)
        graphDB_Session.run(cqlCreate156)
        graphDB_Session.run(cqlCreate157)
        graphDB_Session.run(cqlCreate158)
        graphDB_Session.run(cqlCreate159)
        graphDB_Session.run(cqlCreate160)
        graphDB_Session.run(cqlCreate161)
        graphDB_Session.run(cqlCreate162)
        graphDB_Session.run(cqlCreate164)
        graphDB_Session.run(cqlCreate165)
        graphDB_Session.run(cqlCreate166)
        graphDB_Session.run(cqlCreate167)
        graphDB_Session.run(cqlCreate168)
        graphDB_Session.run(cqlCreate169)
        graphDB_Session.run(cqlCreate170)
        graphDB_Session.run(cqlCreate171)
        graphDB_Session.run(cqlCreate172)
        graphDB_Session.run(cqlCreate173)
        graphDB_Session.run(cqlCreate174)
        graphDB_Session.run(cqlCreate175)
        graphDB_Session.run(cqlCreate176)
        graphDB_Session.run(cqlCreate177)
        graphDB_Session.run(cqlCreate178)
        graphDB_Session.run(cqlCreate179)
        graphDB_Session.run(cqlCreate180)
        graphDB_Session.run(cqlCreate181)
        graphDB_Session.run(cqlCreate182)
        graphDB_Session.run(cqlCreate183)
        graphDB_Session.run(cqlCreate184)
        graphDB_Session.run(cqlCreate185)
        graphDB_Session.run(cqlCreate186)
        graphDB_Session.run(cqlCreate187)
        graphDB_Session.run(cqlCreate188)
        graphDB_Session.run(cqlCreate189)
        graphDB_Session.run(cqlCreate190)
        graphDB_Session.run(cqlCreate191)
        graphDB_Session.run(cqlCreate192)
        graphDB_Session.run(cqlCreate193)
        graphDB_Session.run(cqlCreate194)
        graphDB_Session.run(cqlCreate195)
        graphDB_Session.run(cqlCreate196)
        graphDB_Session.run(cqlCreate197)
        graphDB_Session.run(cqlCreate198)
        graphDB_Session.run(cqlCreate199)
        graphDB_Session.run(cqlCreate200)
        graphDB_Session.run(cqlCreate201)
        graphDB_Session.run(cqlCreate202)
        graphDB_Session.run(cqlCreate203)
        graphDB_Session.run(cqlCreate204)
        graphDB_Session.run(cqlCreate205)
        graphDB_Session.run(cqlCreate206)
        graphDB_Session.run(cqlCreate207)
        graphDB_Session.run(cqlCreate208)
        graphDB_Session.run(cqlCreate209)
        graphDB_Session.run(cqlCreate210)
        graphDB_Session.run(cqlCreate211)
        graphDB_Session.run(cqlCreate212)
        graphDB_Session.run(cqlCreate213)
        graphDB_Session.run(cqlCreate214)
        graphDB_Session.run(cqlCreate215)
        graphDB_Session.run(cqlCreate216)
        graphDB_Session.run(cqlCreate217)
        graphDB_Session.run(cqlCreate218)
        graphDB_Session.run(cqlCreate219)
        graphDB_Session.run(cqlCreate220)
        graphDB_Session.run(cqlCreate221)
        graphDB_Session.run(cqlCreate222)
        graphDB_Session.run(cqlCreate223)
        graphDB_Session.run(cqlCreate224)
        graphDB_Session.run(cqlCreate225)
        graphDB_Session.run(cqlCreate226)
        graphDB_Session.run(cqlCreate227)
        graphDB_Session.run(cqlCreate228)
        graphDB_Session.run(cqlCreate229)
        graphDB_Session.run(cqlCreate230)
        graphDB_Session.run(cqlCreate231)
        graphDB_Session.run(cqlCreate233)
        graphDB_Session.run(cqlCreate234)
        graphDB_Session.run(cqlCreate235)
        graphDB_Session.run(cqlCreate236)
        graphDB_Session.run(cqlCreate237)
        graphDB_Session.run(cqlCreate238)
        graphDB_Session.run(cqlCreate239)
        graphDB_Session.run(cqlCreate240)
        graphDB_Session.run(cqlCreate241)
        graphDB_Session.run(cqlCreate242)
        graphDB_Session.run(cqlCreate243)
        graphDB_Session.run(cqlCreate244)
        graphDB_Session.run(cqlCreate245)
        graphDB_Session.run(cqlCreate246)
        graphDB_Session.run(cqlCreate247)
        graphDB_Session.run(cqlCreate248)
        graphDB_Session.run(cqlCreate249)
        graphDB_Session.run(cqlCreate250)
        graphDB_Session.run(cqlCreate251)
        graphDB_Session.run(cqlCreate252)
        graphDB_Session.run(cqlCreate253)
        graphDB_Session.run(cqlCreate254)
        graphDB_Session.run(cqlCreate255)
        graphDB_Session.run(cqlCreate256)
        graphDB_Session.run(cqlCreate257)
        graphDB_Session.run(cqlCreate258)
        graphDB_Session.run(cqlCreate259)
        graphDB_Session.run(cqlCreate260)
        graphDB_Session.run(cqlCreate261)
        graphDB_Session.run(cqlCreate262)
        graphDB_Session.run(cqlCreate263)
        graphDB_Session.run(cqlCreate264)
        graphDB_Session.run(cqlCreate265)
        graphDB_Session.run(cqlCreate266)
        graphDB_Session.run(cqlCreate267)
        graphDB_Session.run(cqlCreate268)
        graphDB_Session.run(cqlCreate269)
        graphDB_Session.run(cqlCreate270)
        graphDB_Session.run(cqlCreate271)
        graphDB_Session.run(cqlCreate272)
        graphDB_Session.run(cqlCreate273)
        graphDB_Session.run(cqlCreate274)
        graphDB_Session.run(cqlCreate275)
        graphDB_Session.run(cqlCreate276)
        graphDB_Session.run(cqlCreate277)
        graphDB_Session.run(cqlCreate278)
        graphDB_Session.run(cqlCreate279)
        graphDB_Session.run(cqlCreate280)
        graphDB_Session.run(cqlCreate281)
        graphDB_Session.run(cqlCreate282)
        graphDB_Session.run(cqlCreate283)
        graphDB_Session.run(cqlCreate284)
        graphDB_Session.run(cqlCreate285)
        graphDB_Session.run(cqlCreate286)
        graphDB_Session.run(cqlCreate287)
        graphDB_Session.run(cqlCreate288)
        graphDB_Session.run(cqlCreate289)
        graphDB_Session.run(cqlCreate290)
        graphDB_Session.run(cqlCreate292)
        graphDB_Session.run(cqlCreate293)
        graphDB_Session.run(cqlCreate294)
        graphDB_Session.run(cqlCreate295)
        graphDB_Session.run(cqlCreate296)
        graphDB_Session.run(cqlCreate297)
        graphDB_Session.run(cqlCreate298)
        graphDB_Session.run(cqlCreate299)
        graphDB_Session.run(cqlCreate300)
        graphDB_Session.run(cqlCreate301)
        graphDB_Session.run(cqlCreate302)
        graphDB_Session.run(cqlCreate303)
        graphDB_Session.run(cqlCreate304)
        graphDB_Session.run(cqlCreate305)
        graphDB_Session.run(cqlCreate306)
        graphDB_Session.run(cqlCreate307)
        graphDB_Session.run(cqlCreate308)
        graphDB_Session.run(cqlCreate309)
        graphDB_Session.run(cqlCreate310)
        graphDB_Session.run(cqlCreate311)
        graphDB_Session.run(cqlCreate312)
        graphDB_Session.run(cqlCreate313)
        graphDB_Session.run(cqlCreate314)
        graphDB_Session.run(cqlCreate315)
        graphDB_Session.run(cqlCreate316)
        graphDB_Session.run(cqlCreate317)
        graphDB_Session.run(cqlCreate318)
        graphDB_Session.run(cqlCreate319)
        graphDB_Session.run(cqlCreate320)
        graphDB_Session.run(cqlCreate321)
        graphDB_Session.run(cqlCreate322)
        graphDB_Session.run(cqlCreate323)
        graphDB_Session.run(cqlCreate324)
        graphDB_Session.run(cqlCreate325)
        graphDB_Session.run(cqlCreate326)
        graphDB_Session.run(cqlCreate327)
        graphDB_Session.run(cqlCreate328)
        graphDB_Session.run(cqlCreate329)
        graphDB_Session.run(cqlCreate330)
        graphDB_Session.run(cqlCreate331)
        graphDB_Session.run(cqlCreate332)
        graphDB_Session.run(cqlCreate333)
        graphDB_Session.run(cqlCreate334)
        graphDB_Session.run(cqlCreate335)
        graphDB_Session.run(cqlCreate336)
        graphDB_Session.run(cqlCreate337)
        graphDB_Session.run(cqlCreate338)
        graphDB_Session.run(cqlCreate339)
        graphDB_Session.run(cqlCreate340)
        graphDB_Session.run(cqlCreate341)
        graphDB_Session.run(cqlCreate342)
        graphDB_Session.run(cqlCreate343)
        graphDB_Session.run(cqlCreate344)
        graphDB_Session.run(cqlCreate345)
        graphDB_Session.run(cqlCreate346)
        graphDB_Session.run(cqlCreate347)
        graphDB_Session.run(cqlCreate348)
        graphDB_Session.run(cqlCreate349)
        graphDB_Session.run(cqlCreate350)
        graphDB_Session.run(cqlCreate351)
        graphDB_Session.run(cqlCreate352)
        graphDB_Session.run(cqlCreate353)
        graphDB_Session.run(cqlCreate354)
        graphDB_Session.run(cqlCreate355)
        graphDB_Session.run(cqlCreate356)
        graphDB_Session.run(cqlCreate357)
        graphDB_Session.run(cqlCreate358)
        graphDB_Session.run(cqlCreate359)
        graphDB_Session.run(cqlCreate361)
        graphDB_Session.run(cqlCreate362)
        graphDB_Session.run(cqlCreate363)
        graphDB_Session.run(cqlCreate364)
        graphDB_Session.run(cqlCreate365)
        graphDB_Session.run(cqlCreate366)
        graphDB_Session.run(cqlCreate367)
        graphDB_Session.run(cqlCreate368)
        graphDB_Session.run(cqlCreate369)
        graphDB_Session.run(cqlCreate370)
        graphDB_Session.run(cqlCreate371)
        graphDB_Session.run(cqlCreate372)
        graphDB_Session.run(cqlCreate373)
        graphDB_Session.run(cqlCreate374)
        graphDB_Session.run(cqlCreate375)
        graphDB_Session.run(cqlCreate376)
        graphDB_Session.run(cqlCreate377)
        graphDB_Session.run(cqlCreate378)
        graphDB_Session.run(cqlCreate379)
        graphDB_Session.run(cqlCreate380)
        graphDB_Session.run(cqlCreate381)
        graphDB_Session.run(cqlCreate382)
        graphDB_Session.run(cqlCreate383)
        graphDB_Session.run(cqlCreate384)
        graphDB_Session.run(cqlCreate385)
        graphDB_Session.run(cqlCreate386)
        graphDB_Session.run(cqlCreate387)
        graphDB_Session.run(cqlCreate388)
        graphDB_Session.run(cqlCreate389)
        graphDB_Session.run(cqlCreate390)
        graphDB_Session.run(cqlCreate391)
        graphDB_Session.run(cqlCreate392)
        graphDB_Session.run(cqlCreate393)
        graphDB_Session.run(cqlCreate394)
        graphDB_Session.run(cqlCreate395)
        graphDB_Session.run(cqlCreate396)
        graphDB_Session.run(cqlCreate397)
        graphDB_Session.run(cqlCreate398)
        graphDB_Session.run(cqlCreate399)
        graphDB_Session.run(cqlCreate400)
        graphDB_Session.run(cqlCreate401)
        graphDB_Session.run(cqlCreate402)
        graphDB_Session.run(cqlCreate403)
        graphDB_Session.run(cqlCreate404)
        graphDB_Session.run(cqlCreate405)
        graphDB_Session.run(cqlCreate406)
        graphDB_Session.run(cqlCreate407)
        graphDB_Session.run(cqlCreate408)
        graphDB_Session.run(cqlCreate409)
        graphDB_Session.run(cqlCreate410)
        graphDB_Session.run(cqlCreate411)
        graphDB_Session.run(cqlCreate412)
        graphDB_Session.run(cqlCreate413)
        graphDB_Session.run(cqlCreate414)
        graphDB_Session.run(cqlCreate416)
        graphDB_Session.run(cqlCreate417)
        graphDB_Session.run(cqlCreate418)
        graphDB_Session.run(cqlCreate419)
        graphDB_Session.run(cqlCreate420)
        graphDB_Session.run(cqlCreate421)
        graphDB_Session.run(cqlCreate422)
        graphDB_Session.run(cqlCreate423)
        graphDB_Session.run(cqlCreate424)
        graphDB_Session.run(cqlCreate425)
        graphDB_Session.run(cqlCreate426)
        graphDB_Session.run(cqlCreate427)
        graphDB_Session.run(cqlCreate428)
        graphDB_Session.run(cqlCreate429)
        graphDB_Session.run(cqlCreate430)
        graphDB_Session.run(cqlCreate431)
        graphDB_Session.run(cqlCreate432)
        graphDB_Session.run(cqlCreate433)
        graphDB_Session.run(cqlCreate434)
        graphDB_Session.run(cqlCreate435)
        graphDB_Session.run(cqlCreate436)
        graphDB_Session.run(cqlCreate437)
        graphDB_Session.run(cqlCreate438)
        graphDB_Session.run(cqlCreate439)
        graphDB_Session.run(cqlCreate440)
        graphDB_Session.run(cqlCreate441)
        graphDB_Session.run(cqlCreate442)
        graphDB_Session.run(cqlCreate443)
        graphDB_Session.run(cqlCreate444)
        graphDB_Session.run(cqlCreate445)
        graphDB_Session.run(cqlCreate446)
        graphDB_Session.run(cqlCreate447)
        graphDB_Session.run(cqlCreate448)
        graphDB_Session.run(cqlCreate449)
        graphDB_Session.run(cqlCreate450)
        graphDB_Session.run(cqlCreate451)
        graphDB_Session.run(cqlCreate452)
        graphDB_Session.run(cqlCreate453)
        graphDB_Session.run(cqlCreate454)
        graphDB_Session.run(cqlCreate455)
        graphDB_Session.run(cqlCreate456)
        graphDB_Session.run(cqlCreate457)
        graphDB_Session.run(cqlCreate458)
        graphDB_Session.run(cqlCreate459)
        graphDB_Session.run(cqlCreate460)
        graphDB_Session.run(cqlCreate461)
        graphDB_Session.run(cqlCreate462)
        graphDB_Session.run(cqlCreate463)
        graphDB_Session.run(cqlCreate464)
        graphDB_Session.run(cqlCreate466)
        graphDB_Session.run(cqlCreate467)
        graphDB_Session.run(cqlCreate468)
        graphDB_Session.run(cqlCreate469)
        graphDB_Session.run(cqlCreate470)
        graphDB_Session.run(cqlCreate471)
        graphDB_Session.run(cqlCreate472)
        graphDB_Session.run(cqlCreate473)
        graphDB_Session.run(cqlCreate474)
        graphDB_Session.run(cqlCreate475)
        graphDB_Session.run(cqlCreate476)
        graphDB_Session.run(cqlCreate477)
        graphDB_Session.run(cqlCreate478)
        graphDB_Session.run(cqlCreate479)
        graphDB_Session.run(cqlCreate480)
        graphDB_Session.run(cqlCreate481)
        graphDB_Session.run(cqlCreate482)
        graphDB_Session.run(cqlCreate483)
        graphDB_Session.run(cqlCreate484)
        graphDB_Session.run(cqlCreate485)
        graphDB_Session.run(cqlCreate486)
        graphDB_Session.run(cqlCreate487)
        graphDB_Session.run(cqlCreate488)
        graphDB_Session.run(cqlCreate489)
        graphDB_Session.run(cqlCreate490)
        graphDB_Session.run(cqlCreate491)
        graphDB_Session.run(cqlCreate492)
        graphDB_Session.run(cqlCreate493)
        graphDB_Session.run(cqlCreate494)
        graphDB_Session.run(cqlCreate495)
        graphDB_Session.run(cqlCreate496)
        graphDB_Session.run(cqlCreate497)
        graphDB_Session.run(cqlCreate498)
        graphDB_Session.run(cqlCreate499)
        graphDB_Session.run(cqlCreate500)
        graphDB_Session.run(cqlCreate501)
        graphDB_Session.run(cqlCreate502)
        graphDB_Session.run(cqlCreate503)
        graphDB_Session.run(cqlCreate504)
        graphDB_Session.run(cqlCreate505)
        graphDB_Session.run(cqlCreate506)
        graphDB_Session.run(cqlCreate507)
        graphDB_Session.run(cqlCreate508)
        graphDB_Session.run(cqlCreate509)
        graphDB_Session.run(cqlCreate510)
        graphDB_Session.run(cqlCreate511)
        graphDB_Session.run(cqlCreate512)
        graphDB_Session.run(cqlCreate513)
        graphDB_Session.run(cqlCreate514)
        graphDB_Session.run(cqlCreate515)
        graphDB_Session.run(cqlCreate516)
        graphDB_Session.run(cqlCreate517)
        graphDB_Session.run(cqlCreate518)
        graphDB_Session.run(cqlCreate519)
        graphDB_Session.run(cqlCreate520)
        graphDB_Session.run(cqlCreate521)
        graphDB_Session.run(cqlCreate522)
        graphDB_Session.run(cqlCreate523)
        graphDB_Session.run(cqlCreate524)
        graphDB_Session.run(cqlCreate525)
        graphDB_Session.run(cqlCreate526)
        graphDB_Session.run(cqlCreate527)
        graphDB_Session.run(cqlCreate528)
        graphDB_Session.run(cqlCreate529)
        graphDB_Session.run(cqlCreate530)
        graphDB_Session.run(cqlCreate531)
        graphDB_Session.run(cqlCreate532)
        graphDB_Session.run(cqlCreate533)
        graphDB_Session.run(cqlCreate535)
        graphDB_Session.run(cqlCreate536)
        graphDB_Session.run(cqlCreate537)
        graphDB_Session.run(cqlCreate538)
        graphDB_Session.run(cqlCreate539)
        graphDB_Session.run(cqlCreate540)
        graphDB_Session.run(cqlCreate541)
        graphDB_Session.run(cqlCreate542)
        graphDB_Session.run(cqlCreate543)
        graphDB_Session.run(cqlCreate544)
        graphDB_Session.run(cqlCreate545)
        graphDB_Session.run(cqlCreate546)
        graphDB_Session.run(cqlCreate547)
        graphDB_Session.run(cqlCreate549)
        graphDB_Session.run(cqlCreate550)
        graphDB_Session.run(cqlCreate551)
        graphDB_Session.run(cqlCreate552)
        graphDB_Session.run(cqlCreate553)
        graphDB_Session.run(cqlCreate554)
        graphDB_Session.run(cqlCreate555)
        graphDB_Session.run(cqlCreate556)
        graphDB_Session.run(cqlCreate557)
        graphDB_Session.run(cqlCreate558)
        graphDB_Session.run(cqlCreate559)
        graphDB_Session.run(cqlCreate560)
        graphDB_Session.run(cqlCreate561)
        graphDB_Session.run(cqlCreate562)
        graphDB_Session.run(cqlCreate563)
        graphDB_Session.run(cqlCreate564)
        graphDB_Session.run(cqlCreate565)
        graphDB_Session.run(cqlCreate566)
        graphDB_Session.run(cqlCreate567)
        graphDB_Session.run(cqlCreate568)
        graphDB_Session.run(cqlCreate569)
        graphDB_Session.run(cqlCreate570)
        graphDB_Session.run(cqlCreate571)
        graphDB_Session.run(cqlCreate572)
        graphDB_Session.run(cqlCreate573)
        graphDB_Session.run(cqlCreate574)
        graphDB_Session.run(cqlCreate575)
        graphDB_Session.run(cqlCreate576)
        graphDB_Session.run(cqlCreate577)
        graphDB_Session.run(cqlCreate578)
        graphDB_Session.run(cqlCreate579)
        graphDB_Session.run(cqlCreate580)
        graphDB_Session.run(cqlCreate582)
        graphDB_Session.run(cqlCreate583)
        graphDB_Session.run(cqlCreate584)
        graphDB_Session.run(cqlCreate585)
        graphDB_Session.run(cqlCreate586)
        graphDB_Session.run(cqlCreate587)
        graphDB_Session.run(cqlCreate588)
        graphDB_Session.run(cqlCreate589)
        graphDB_Session.run(cqlCreate590)
        graphDB_Session.run(cqlCreate591)
        graphDB_Session.run(cqlCreate592)
        graphDB_Session.run(cqlCreate593)
        graphDB_Session.run(cqlCreate595)
        graphDB_Session.run(cqlCreate596)
        graphDB_Session.run(cqlCreate597)
        graphDB_Session.run(cqlCreate598)
        graphDB_Session.run(cqlCreate599)
        graphDB_Session.run(cqlCreate600)
        graphDB_Session.run(cqlCreate601)
        graphDB_Session.run(cqlCreate602)
        graphDB_Session.run(cqlCreate603)
#create_relationships()
