import pandas as pd
from py2neo import Graph
from shapely.wkt import loads
from shapely.geometry import Point


# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

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
# div_names()


# Function to create a relationship between the locations of the OtherNames_0 file and the LOCATIONS node.
def check_locations_0():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_0.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Connect to Neo4j
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_0()


def check_locations_1():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_1.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_1()


def check_locations_2():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_2.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_2()


def check_locations_3():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_3.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_3()


def check_locations_4():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_4.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_4()


def check_locations_5():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_5.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_5()


def check_locations_6():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_6.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_6()


def check_locations_7():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_7.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_7()


def check_locations_8():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_8.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_8()


def check_locations_9():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_9.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_9()


def check_locations_10():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_10.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_10()


def check_locations_11():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_11.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_11()


def check_locations_12():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_12.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\nordeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        nordeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\norte.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sudeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sudeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sul.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\centro-oeste.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        centro_oeste_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ac.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        acre_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\al.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        alagoas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\am.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amazonas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ap.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        amapa_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ba.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        bahia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ce.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        ceara_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\df.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        distrito_federal_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\es.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        espirito_santo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\go.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        goias_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ma.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        maranhao_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mg.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        minas_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ms.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\mt.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        mato_grosso_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pa.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        para_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pb.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        paraiba_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pe.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        pernambuco_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pi.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        piaui_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\pr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        parana_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rj.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rn.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_norte_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\ro.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rondonia_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rr.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        roraima_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\rs.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        rio_g_sul_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sc.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        santa_catarina_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\se.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sergipe_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\sp.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        sao_paulo_polygon = loads(wkt_data)

    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\to.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        tocantins_polygon = loads(wkt_data)

    # Loop through each row in the CSV file
    for index, row in df.iterrows():
        # Extract latitude and longitude values from the CSV data
        latitude = row["latitude"]
        longitude = row["longitude"]

        # Create a shapely Point object from the coordinates
        point = Point(longitude, latitude)

        # Check if the point is inside the Brazil boundary polygon
        if brazil_polygon.contains(point):
            # If the point is inside the polygon, create a relationship in Neo4j
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_COUNTRY]->(b)'
            graph.run(query)

            print(f"Relationship created for {row['name']} with Brazil")

            # Check if the point is inside the Regions and States boundary polygon
            if nordeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Nordeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Nordeste")

                if alagoas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Alagoas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Alagoas")
                else:
                    print(f"{row['name']} don't match with Alagoas:", point)

                if bahia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Bahia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Bahia")
                else:
                    print(f"{row['name']} don't match with Bahia:", point)

                if ceara_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Ceará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Ceará")
                else:
                    print(f"{row['name']} don't match with Ceará:", point)

                if maranhao_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Maranhão" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Pernambuco")
                else:
                    print(f"{row['name']} don't match with Pernambuco:", point)

                if piaui_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Piauí" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Piauí")
                else:
                    print(f"{row['name']} don't match with Piauí:", point)

                if rio_g_norte_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Norte:", point)

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Sergipe")
                else:
                    print(f"{row['name']} don't match with Sergipe:", point)
            else:
                print(f"{row['name']} don't match with Nordeste:", point)

            if norte_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Norte" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Norte")

                # Check if the point is inside the States boundary polygon
                if acre_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Acre" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Acre")
                else:
                    print(f"{row['name']} don't match with Acre:", point)

                if amazonas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amazonas" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Amazonas")
                else:
                    print(f"{row['name']} don't match with Amazonas:", point)

                if amapa_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Amapá" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Amapá")
                else:
                    print(f"{row['name']} don't match with Amapá:", point)

                if rondonia_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rondônia" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point)

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Tocantins")
                else:
                    print(f"{row['name']} don't match with Tocantins:", point)

                if para_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pará" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pará")
                else:
                    print(f"{row['name']} don't match with Pará:", point)
            else:
                print(f"{row['name']} don't match with Norte:", point)

            if sudeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sudeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sudeste")

                if espirito_santo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Espírito Santo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(
                        f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(
                        f"{row['name']} don't match with Minas Gerais:", point)

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(
                        f"{row['name']} don't match with Rio de Janeiro:", point)

            else:
                print(f"{row['name']} don't match Sudeste:", point)

            if sul_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Sul")

                if rio_g_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio Grande do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Rio Grande do Sul:", point)

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(
                        f"{row['name']} don't match with Santa Catarina:", point)

            else:
                print(f"{row['name']} don't match with Sul:", point)

            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(
                    f"Relationship created for {row['name']} with Centro-Oeste")

                if goias_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Goiás" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Goiás")
                else:
                    print(f"{row['name']} don't match with Goiás:", point)

                if mato_sul_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso do Sul" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso do Sul:", point)

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(
                        f"{row['name']} don't match with Mato Grosso:", point)

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(
                        f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(
                        f"{row['name']} don't match with Distrito Federal:", point)

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)
# check_locations_12()

# Create main nodes:


def create_nodes():
    with graph.session() as graph:
        graph.run(cqlCreate0)
        graph.run(cqlCreate47)
        graph.run(cqlCreate105)
        graph.run(cqlCreate163)
        graph.run(cqlCreate232)
        graph.run(cqlCreate291)
        graph.run(cqlCreate360)
        graph.run(cqlCreate415)
        graph.run(cqlCreate465)
        graph.run(cqlCreate534)
        graph.run(cqlCreate548)
        graph.run(cqlCreate581)
        graph.run(cqlCreate594)
        graph.run(cqlCreate604)
        graph.run(cqlCreate605)
        graph.run(cqlCreate606)
# create_nodes()

# Create main indexes


def create_indexes():
    with graph.session() as graph:
        graph.run(cqlCreate00)
        graph.run(cqlCreate01)
        graph.run(cqlCreate02)
        graph.run(cqlCreate03)
        graph.run(cqlCreate04)
        graph.run(cqlCreate05)
        graph.run(cqlCreate06)
        graph.run(cqlCreate07)
        graph.run(cqlCreate08)
        graph.run(cqlCreate09)
        graph.run(cqlCreate010)
        graph.run(cqlCreate011)
        graph.run(cqlCreate012)
        graph.run(cqlCreate013)
        graph.run(cqlCreate014)
        graph.run(cqlCreate015)
        graph.run(cqlCreate016)
        graph.run(cqlCreate017)
        graph.run(cqlCreate018)
        graph.run(cqlCreate019)
        graph.run(cqlCreate020)
        graph.run(cqlCreate021)
        graph.run(cqlCreate022)
        graph.run(cqlCreate023)
        graph.run(cqlCreate024)
        graph.run(cqlCreate025)
        graph.run(cqlCreate026)
        graph.run(cqlCreate027)
        graph.run(cqlCreate028)
        graph.run(cqlCreate029)
        graph.run(cqlCreate030)
        graph.run(cqlCreate031)
        graph.run(cqlCreate032)
        graph.run(cqlCreate033)
        graph.run(cqlCreate034)
        graph.run(cqlCreate035)
        graph.run(cqlCreate036)
        graph.run(cqlCreate037)
        graph.run(cqlCreate038)
        graph.run(cqlCreate039)
        graph.run(cqlCreate040)
        graph.run(cqlCreate041)
        graph.run(cqlCreate042)
        graph.run(cqlCreate043)
        graph.run(cqlCreate044)
        graph.run(cqlCreate045)
        graph.run(cqlCreate046)
        graph.run(cqlCreate047)
        graph.run(cqlCreate048)
        graph.run(cqlCreate049)
        graph.run(cqlCreate050)
        graph.run(cqlCreate051)
        graph.run(cqlCreate052)
        graph.run(cqlCreate053)
        graph.run(cqlCreate054)
        graph.run(cqlCreate055)
        graph.run(cqlCreate056)
        graph.run(cqlCreate057)
        graph.run(cqlCreate058)
        graph.run(cqlCreate059)
        graph.run(cqlCreate060)
        graph.run(cqlCreate061)
        graph.run(cqlCreate062)
        graph.run(cqlCreate063)
        graph.run(cqlCreate064)
        graph.run(cqlCreate065)
        graph.run(cqlCreate066)
        graph.run(cqlCreate067)
        graph.run(cqlCreate068)
        graph.run(cqlCreate069)
        graph.run(cqlCreate070)
        graph.run(cqlCreate071)
# create_indexes()


# Create main realtionships
def create_relationships():
    graph.run(cqlCreate1)
    graph.run(cqlCreate2)
    graph.run(cqlCreate3)
    graph.run(cqlCreate4)
    graph.run(cqlCreate5)
    graph.run(cqlCreate6)
    graph.run(cqlCreate7)
    graph.run(cqlCreate8)
    graph.run(cqlCreate9)
    graph.run(cqlCreate10)
    graph.run(cqlCreate11)
    graph.run(cqlCreate12)
    graph.run(cqlCreate13)
    graph.run(cqlCreate14)
    graph.run(cqlCreate15)
    graph.run(cqlCreate16)
    graph.run(cqlCreate17)
    graph.run(cqlCreate18)
    graph.run(cqlCreate19)
    graph.run(cqlCreate20)
    graph.run(cqlCreate21)
    graph.run(cqlCreate22)
    graph.run(cqlCreate23)
    graph.run(cqlCreate24)
    graph.run(cqlCreate25)
    graph.run(cqlCreate26)
    graph.run(cqlCreate27)
    graph.run(cqlCreate28)
    graph.run(cqlCreate29)
    graph.run(cqlCreate30)
    graph.run(cqlCreate31)
    graph.run(cqlCreate32)
    graph.run(cqlCreate33)
    graph.run(cqlCreate34)
    graph.run(cqlCreate35)
    graph.run(cqlCreate36)
    graph.run(cqlCreate37)
    graph.run(cqlCreate38)
    graph.run(cqlCreate39)
    graph.run(cqlCreate40)
    graph.run(cqlCreate41)
    graph.run(cqlCreate42)
    graph.run(cqlCreate43)
    graph.run(cqlCreate44)
    graph.run(cqlCreate45)
    graph.run(cqlCreate46)
    graph.run(cqlCreate48)
    graph.run(cqlCreate49)
    graph.run(cqlCreate50)
    graph.run(cqlCreate51)
    graph.run(cqlCreate52)
    graph.run(cqlCreate53)
    graph.run(cqlCreate54)
    graph.run(cqlCreate55)
    graph.run(cqlCreate56)
    graph.run(cqlCreate57)
    graph.run(cqlCreate58)
    graph.run(cqlCreate59)
    graph.run(cqlCreate60)
    graph.run(cqlCreate61)
    graph.run(cqlCreate62)
    graph.run(cqlCreate63)
    graph.run(cqlCreate64)
    graph.run(cqlCreate65)
    graph.run(cqlCreate66)
    graph.run(cqlCreate67)
    graph.run(cqlCreate68)
    graph.run(cqlCreate69)
    graph.run(cqlCreate70)
    graph.run(cqlCreate71)
    graph.run(cqlCreate72)
    graph.run(cqlCreate73)
    graph.run(cqlCreate74)
    graph.run(cqlCreate75)
    graph.run(cqlCreate76)
    graph.run(cqlCreate77)
    graph.run(cqlCreate78)
    graph.run(cqlCreate79)
    graph.run(cqlCreate80)
    graph.run(cqlCreate81)
    graph.run(cqlCreate82)
    graph.run(cqlCreate83)
    graph.run(cqlCreate84)
    graph.run(cqlCreate85)
    graph.run(cqlCreate86)
    graph.run(cqlCreate87)
    graph.run(cqlCreate88)
    graph.run(cqlCreate89)
    graph.run(cqlCreate90)
    graph.run(cqlCreate91)
    graph.run(cqlCreate92)
    graph.run(cqlCreate93)
    graph.run(cqlCreate94)
    graph.run(cqlCreate95)
    graph.run(cqlCreate96)
    graph.run(cqlCreate97)
    graph.run(cqlCreate98)
    graph.run(cqlCreate99)
    graph.run(cqlCreate100)
    graph.run(cqlCreate101)
    graph.run(cqlCreate102)
    graph.run(cqlCreate103)
    graph.run(cqlCreate104)
    graph.run(cqlCreate106)
    graph.run(cqlCreate107)
    graph.run(cqlCreate108)
    graph.run(cqlCreate109)
    graph.run(cqlCreate110)
    graph.run(cqlCreate111)
    graph.run(cqlCreate112)
    graph.run(cqlCreate113)
    graph.run(cqlCreate114)
    graph.run(cqlCreate115)
    graph.run(cqlCreate116)
    graph.run(cqlCreate117)
    graph.run(cqlCreate118)
    graph.run(cqlCreate119)
    graph.run(cqlCreate120)
    graph.run(cqlCreate121)
    graph.run(cqlCreate122)
    graph.run(cqlCreate123)
    graph.run(cqlCreate124)
    graph.run(cqlCreate125)
    graph.run(cqlCreate126)
    graph.run(cqlCreate127)
    graph.run(cqlCreate128)
    graph.run(cqlCreate129)
    graph.run(cqlCreate130)
    graph.run(cqlCreate131)
    graph.run(cqlCreate132)
    graph.run(cqlCreate133)
    graph.run(cqlCreate134)
    graph.run(cqlCreate135)
    graph.run(cqlCreate136)
    graph.run(cqlCreate137)
    graph.run(cqlCreate138)
    graph.run(cqlCreate139)
    graph.run(cqlCreate140)
    graph.run(cqlCreate141)
    graph.run(cqlCreate142)
    graph.run(cqlCreate143)
    graph.run(cqlCreate144)
    graph.run(cqlCreate145)
    graph.run(cqlCreate146)
    graph.run(cqlCreate147)
    graph.run(cqlCreate148)
    graph.run(cqlCreate149)
    graph.run(cqlCreate150)
    graph.run(cqlCreate151)
    graph.run(cqlCreate152)
    graph.run(cqlCreate153)
    graph.run(cqlCreate154)
    graph.run(cqlCreate155)
    graph.run(cqlCreate156)
    graph.run(cqlCreate157)
    graph.run(cqlCreate158)
    graph.run(cqlCreate159)
    graph.run(cqlCreate160)
    graph.run(cqlCreate161)
    graph.run(cqlCreate162)
    graph.run(cqlCreate164)
    graph.run(cqlCreate165)
    graph.run(cqlCreate166)
    graph.run(cqlCreate167)
    graph.run(cqlCreate168)
    graph.run(cqlCreate169)
    graph.run(cqlCreate170)
    graph.run(cqlCreate171)
    graph.run(cqlCreate172)
    graph.run(cqlCreate173)
    graph.run(cqlCreate174)
    graph.run(cqlCreate175)
    graph.run(cqlCreate176)
    graph.run(cqlCreate177)
    graph.run(cqlCreate178)
    graph.run(cqlCreate179)
    graph.run(cqlCreate180)
    graph.run(cqlCreate181)
    graph.run(cqlCreate182)
    graph.run(cqlCreate183)
    graph.run(cqlCreate184)
    graph.run(cqlCreate185)
    graph.run(cqlCreate186)
    graph.run(cqlCreate187)
    graph.run(cqlCreate188)
    graph.run(cqlCreate189)
    graph.run(cqlCreate190)
    graph.run(cqlCreate191)
    graph.run(cqlCreate192)
    graph.run(cqlCreate193)
    graph.run(cqlCreate194)
    graph.run(cqlCreate195)
    graph.run(cqlCreate196)
    graph.run(cqlCreate197)
    graph.run(cqlCreate198)
    graph.run(cqlCreate199)
    graph.run(cqlCreate200)
    graph.run(cqlCreate201)
    graph.run(cqlCreate202)
    graph.run(cqlCreate203)
    graph.run(cqlCreate204)
    graph.run(cqlCreate205)
    graph.run(cqlCreate206)
    graph.run(cqlCreate207)
    graph.run(cqlCreate208)
    graph.run(cqlCreate209)
    graph.run(cqlCreate210)
    graph.run(cqlCreate211)
    graph.run(cqlCreate212)
    graph.run(cqlCreate213)
    graph.run(cqlCreate214)
    graph.run(cqlCreate215)
    graph.run(cqlCreate216)
    graph.run(cqlCreate217)
    graph.run(cqlCreate218)
    graph.run(cqlCreate219)
    graph.run(cqlCreate220)
    graph.run(cqlCreate221)
    graph.run(cqlCreate222)
    graph.run(cqlCreate223)
    graph.run(cqlCreate224)
    graph.run(cqlCreate225)
    graph.run(cqlCreate226)
    graph.run(cqlCreate227)
    graph.run(cqlCreate228)
    graph.run(cqlCreate229)
    graph.run(cqlCreate230)
    graph.run(cqlCreate231)
    graph.run(cqlCreate233)
    graph.run(cqlCreate234)
    graph.run(cqlCreate235)
    graph.run(cqlCreate236)
    graph.run(cqlCreate237)
    graph.run(cqlCreate238)
    graph.run(cqlCreate239)
    graph.run(cqlCreate240)
    graph.run(cqlCreate241)
    graph.run(cqlCreate242)
    graph.run(cqlCreate243)
    graph.run(cqlCreate244)
    graph.run(cqlCreate245)
    graph.run(cqlCreate246)
    graph.run(cqlCreate247)
    graph.run(cqlCreate248)
    graph.run(cqlCreate249)
    graph.run(cqlCreate250)
    graph.run(cqlCreate251)
    graph.run(cqlCreate252)
    graph.run(cqlCreate253)
    graph.run(cqlCreate254)
    graph.run(cqlCreate255)
    graph.run(cqlCreate256)
    graph.run(cqlCreate257)
    graph.run(cqlCreate258)
    graph.run(cqlCreate259)
    graph.run(cqlCreate260)
    graph.run(cqlCreate261)
    graph.run(cqlCreate262)
    graph.run(cqlCreate263)
    graph.run(cqlCreate264)
    graph.run(cqlCreate265)
    graph.run(cqlCreate266)
    graph.run(cqlCreate267)
    graph.run(cqlCreate268)
    graph.run(cqlCreate269)
    graph.run(cqlCreate270)
    graph.run(cqlCreate271)
    graph.run(cqlCreate272)
    graph.run(cqlCreate273)
    graph.run(cqlCreate274)
    graph.run(cqlCreate275)
    graph.run(cqlCreate276)
    graph.run(cqlCreate277)
    graph.run(cqlCreate278)
    graph.run(cqlCreate279)
    graph.run(cqlCreate280)
    graph.run(cqlCreate281)
    graph.run(cqlCreate282)
    graph.run(cqlCreate283)
    graph.run(cqlCreate284)
    graph.run(cqlCreate285)
    graph.run(cqlCreate286)
    graph.run(cqlCreate287)
    graph.run(cqlCreate288)
    graph.run(cqlCreate289)
    graph.run(cqlCreate290)
    graph.run(cqlCreate292)
    graph.run(cqlCreate293)
    graph.run(cqlCreate294)
    graph.run(cqlCreate295)
    graph.run(cqlCreate296)
    graph.run(cqlCreate297)
    graph.run(cqlCreate298)
    graph.run(cqlCreate299)
    graph.run(cqlCreate300)
    graph.run(cqlCreate301)
    graph.run(cqlCreate302)
    graph.run(cqlCreate303)
    graph.run(cqlCreate304)
    graph.run(cqlCreate305)
    graph.run(cqlCreate306)
    graph.run(cqlCreate307)
    graph.run(cqlCreate308)
    graph.run(cqlCreate309)
    graph.run(cqlCreate310)
    graph.run(cqlCreate311)
    graph.run(cqlCreate312)
    graph.run(cqlCreate313)
    graph.run(cqlCreate314)
    graph.run(cqlCreate315)
    graph.run(cqlCreate316)
    graph.run(cqlCreate317)
    graph.run(cqlCreate318)
    graph.run(cqlCreate319)
    graph.run(cqlCreate320)
    graph.run(cqlCreate321)
    graph.run(cqlCreate322)
    graph.run(cqlCreate323)
    graph.run(cqlCreate324)
    graph.run(cqlCreate325)
    graph.run(cqlCreate326)
    graph.run(cqlCreate327)
    graph.run(cqlCreate328)
    graph.run(cqlCreate329)
    graph.run(cqlCreate330)
    graph.run(cqlCreate331)
    graph.run(cqlCreate332)
    graph.run(cqlCreate333)
    graph.run(cqlCreate334)
    graph.run(cqlCreate335)
    graph.run(cqlCreate336)
    graph.run(cqlCreate337)
    graph.run(cqlCreate338)
    graph.run(cqlCreate339)
    graph.run(cqlCreate340)
    graph.run(cqlCreate341)
    graph.run(cqlCreate342)
    graph.run(cqlCreate343)
    graph.run(cqlCreate344)
    graph.run(cqlCreate345)
    graph.run(cqlCreate346)
    graph.run(cqlCreate347)
    graph.run(cqlCreate348)
    graph.run(cqlCreate349)
    graph.run(cqlCreate350)
    graph.run(cqlCreate351)
    graph.run(cqlCreate352)
    graph.run(cqlCreate353)
    graph.run(cqlCreate354)
    graph.run(cqlCreate355)
    graph.run(cqlCreate356)
    graph.run(cqlCreate357)
    graph.run(cqlCreate358)
    graph.run(cqlCreate359)
    graph.run(cqlCreate361)
    graph.run(cqlCreate362)
    graph.run(cqlCreate363)
    graph.run(cqlCreate364)
    graph.run(cqlCreate365)
    graph.run(cqlCreate366)
    graph.run(cqlCreate367)
    graph.run(cqlCreate368)
    graph.run(cqlCreate369)
    graph.run(cqlCreate370)
    graph.run(cqlCreate371)
    graph.run(cqlCreate372)
    graph.run(cqlCreate373)
    graph.run(cqlCreate374)
    graph.run(cqlCreate375)
    graph.run(cqlCreate376)
    graph.run(cqlCreate377)
    graph.run(cqlCreate378)
    graph.run(cqlCreate379)
    graph.run(cqlCreate380)
    graph.run(cqlCreate381)
    graph.run(cqlCreate382)
    graph.run(cqlCreate383)
    graph.run(cqlCreate384)
    graph.run(cqlCreate385)
    graph.run(cqlCreate386)
    graph.run(cqlCreate387)
    graph.run(cqlCreate388)
    graph.run(cqlCreate389)
    graph.run(cqlCreate390)
    graph.run(cqlCreate391)
    graph.run(cqlCreate392)
    graph.run(cqlCreate393)
    graph.run(cqlCreate394)
    graph.run(cqlCreate395)
    graph.run(cqlCreate396)
    graph.run(cqlCreate397)
    graph.run(cqlCreate398)
    graph.run(cqlCreate399)
    graph.run(cqlCreate400)
    graph.run(cqlCreate401)
    graph.run(cqlCreate402)
    graph.run(cqlCreate403)
    graph.run(cqlCreate404)
    graph.run(cqlCreate405)
    graph.run(cqlCreate406)
    graph.run(cqlCreate407)
    graph.run(cqlCreate408)
    graph.run(cqlCreate409)
    graph.run(cqlCreate410)
    graph.run(cqlCreate411)
    graph.run(cqlCreate412)
    graph.run(cqlCreate413)
    graph.run(cqlCreate414)
    graph.run(cqlCreate416)
    graph.run(cqlCreate417)
    graph.run(cqlCreate418)
    graph.run(cqlCreate419)
    graph.run(cqlCreate420)
    graph.run(cqlCreate421)
    graph.run(cqlCreate422)
    graph.run(cqlCreate423)
    graph.run(cqlCreate424)
    graph.run(cqlCreate425)
    graph.run(cqlCreate426)
    graph.run(cqlCreate427)
    graph.run(cqlCreate428)
    graph.run(cqlCreate429)
    graph.run(cqlCreate430)
    graph.run(cqlCreate431)
    graph.run(cqlCreate432)
    graph.run(cqlCreate433)
    graph.run(cqlCreate434)
    graph.run(cqlCreate435)
    graph.run(cqlCreate436)
    graph.run(cqlCreate437)
    graph.run(cqlCreate438)
    graph.run(cqlCreate439)
    graph.run(cqlCreate440)
    graph.run(cqlCreate441)
    graph.run(cqlCreate442)
    graph.run(cqlCreate443)
    graph.run(cqlCreate444)
    graph.run(cqlCreate445)
    graph.run(cqlCreate446)
    graph.run(cqlCreate447)
    graph.run(cqlCreate448)
    graph.run(cqlCreate449)
    graph.run(cqlCreate450)
    graph.run(cqlCreate451)
    graph.run(cqlCreate452)
    graph.run(cqlCreate453)
    graph.run(cqlCreate454)
    graph.run(cqlCreate455)
    graph.run(cqlCreate456)
    graph.run(cqlCreate457)
    graph.run(cqlCreate458)
    graph.run(cqlCreate459)
    graph.run(cqlCreate460)
    graph.run(cqlCreate461)
    graph.run(cqlCreate462)
    graph.run(cqlCreate463)
    graph.run(cqlCreate464)
    graph.run(cqlCreate466)
    graph.run(cqlCreate467)
    graph.run(cqlCreate468)
    graph.run(cqlCreate469)
    graph.run(cqlCreate470)
    graph.run(cqlCreate471)
    graph.run(cqlCreate472)
    graph.run(cqlCreate473)
    graph.run(cqlCreate474)
    graph.run(cqlCreate475)
    graph.run(cqlCreate476)
    graph.run(cqlCreate477)
    graph.run(cqlCreate478)
    graph.run(cqlCreate479)
    graph.run(cqlCreate480)
    graph.run(cqlCreate481)
    graph.run(cqlCreate482)
    graph.run(cqlCreate483)
    graph.run(cqlCreate484)
    graph.run(cqlCreate485)
    graph.run(cqlCreate486)
    graph.run(cqlCreate487)
    graph.run(cqlCreate488)
    graph.run(cqlCreate489)
    graph.run(cqlCreate490)
    graph.run(cqlCreate491)
    graph.run(cqlCreate492)
    graph.run(cqlCreate493)
    graph.run(cqlCreate494)
    graph.run(cqlCreate495)
    graph.run(cqlCreate496)
    graph.run(cqlCreate497)
    graph.run(cqlCreate498)
    graph.run(cqlCreate499)
    graph.run(cqlCreate500)
    graph.run(cqlCreate501)
    graph.run(cqlCreate502)
    graph.run(cqlCreate503)
    graph.run(cqlCreate504)
    graph.run(cqlCreate505)
    graph.run(cqlCreate506)
    graph.run(cqlCreate507)
    graph.run(cqlCreate508)
    graph.run(cqlCreate509)
    graph.run(cqlCreate510)
    graph.run(cqlCreate511)
    graph.run(cqlCreate512)
    graph.run(cqlCreate513)
    graph.run(cqlCreate514)
    graph.run(cqlCreate515)
    graph.run(cqlCreate516)
    graph.run(cqlCreate517)
    graph.run(cqlCreate518)
    graph.run(cqlCreate519)
    graph.run(cqlCreate520)
    graph.run(cqlCreate521)
    graph.run(cqlCreate522)
    graph.run(cqlCreate523)
    graph.run(cqlCreate524)
    graph.run(cqlCreate525)
    graph.run(cqlCreate526)
    graph.run(cqlCreate527)
    graph.run(cqlCreate528)
    graph.run(cqlCreate529)
    graph.run(cqlCreate530)
    graph.run(cqlCreate531)
    graph.run(cqlCreate532)
    graph.run(cqlCreate533)
    graph.run(cqlCreate535)
    graph.run(cqlCreate536)
    graph.run(cqlCreate537)
    graph.run(cqlCreate538)
    graph.run(cqlCreate539)
    graph.run(cqlCreate540)
    graph.run(cqlCreate541)
    graph.run(cqlCreate542)
    graph.run(cqlCreate543)
    graph.run(cqlCreate544)
    graph.run(cqlCreate545)
    graph.run(cqlCreate546)
    graph.run(cqlCreate547)
    graph.run(cqlCreate549)
    graph.run(cqlCreate550)
    graph.run(cqlCreate551)
    graph.run(cqlCreate552)
    graph.run(cqlCreate553)
    graph.run(cqlCreate554)
    graph.run(cqlCreate555)
    graph.run(cqlCreate556)
    graph.run(cqlCreate557)
    graph.run(cqlCreate558)
    graph.run(cqlCreate559)
    graph.run(cqlCreate560)
    graph.run(cqlCreate561)
    graph.run(cqlCreate562)
    graph.run(cqlCreate563)
    graph.run(cqlCreate564)
    graph.run(cqlCreate565)
    graph.run(cqlCreate566)
    graph.run(cqlCreate567)
    graph.run(cqlCreate568)
    graph.run(cqlCreate569)
    graph.run(cqlCreate570)
    graph.run(cqlCreate571)
    graph.run(cqlCreate572)
    graph.run(cqlCreate573)
    graph.run(cqlCreate574)
    graph.run(cqlCreate575)
    graph.run(cqlCreate576)
    graph.run(cqlCreate577)
    graph.run(cqlCreate578)
    graph.run(cqlCreate579)
    graph.run(cqlCreate580)
    graph.run(cqlCreate582)
    graph.run(cqlCreate583)
    graph.run(cqlCreate584)
    graph.run(cqlCreate585)
    graph.run(cqlCreate586)
    graph.run(cqlCreate587)
    graph.run(cqlCreate588)
    graph.run(cqlCreate589)
    graph.run(cqlCreate590)
    graph.run(cqlCreate591)
    graph.run(cqlCreate592)
    graph.run(cqlCreate593)
    graph.run(cqlCreate595)
    graph.run(cqlCreate596)
    graph.run(cqlCreate597)
    graph.run(cqlCreate598)
    graph.run(cqlCreate599)
    graph.run(cqlCreate600)
    graph.run(cqlCreate601)
    graph.run(cqlCreate602)
    graph.run(cqlCreate603)
#create_relationships()
