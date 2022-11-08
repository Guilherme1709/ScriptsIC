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

                WITH linha WHERE NOT linha.othername41 IS null
                CREATE (other:othername41{othername41:linha.othername41})

                WITH linha WHERE NOT linha.othername42 IS null
                CREATE (other42:othername42{othername42:linha.othername42})

                WITH linha WHERE NOT linha.othername43 IS null
                CREATE (other43:othername43{othername43:linha.othername43})

                WITH linha WHERE NOT linha.othername44 IS null
                CREATE (other44:othername44{othername44:linha.othername44})

                WITH linha WHERE NOT linha.othername45 IS null
                CREATE (other45:othername45{othername45:linha.othername45})

                WITH linha WHERE NOT linha.othername46 IS null
                CREATE (other46:othername46{othername46:linha.othername46})

                WITH linha WHERE NOT linha.othername47 IS null
                CREATE (other47:othername47{othername47:linha.othername47})
                
                WITH linha WHERE NOT linha.othername48 IS null
                CREATE (other48:othername48{othername48:linha.othername48})

                WITH linha WHERE NOT linha.othername49 IS null
                CREATE (other49:othername49{othername49:linha.othername49})

                WITH linha WHERE NOT linha.othername50 IS null
                CREATE (other50:othername50{othername50:linha.othername50})

                WITH linha WHERE NOT linha.othername51 IS null
                CREATE (other51:othername51{othername51:linha.othername51})

                WITH linha WHERE NOT linha.othername52 IS null
                CREATE (other52:othername52{othername52:linha.othername52})

                WITH linha WHERE NOT linha.othername53 IS null
                CREATE (other53:othername53{othername53:linha.othername53})

                WITH linha WHERE NOT linha.othername54 IS null
                CREATE (other54:othername54{othername54:linha.othername54})

                WITH linha WHERE NOT linha.othername55 IS null
                CREATE (other55:othername55{othername55:linha.othername55})

                WITH linha WHERE NOT linha.othername56 IS null
                CREATE (other56:othername56{othername56:linha.othername56})

                WITH linha WHERE NOT linha.othername57 IS null
                CREATE (other57:othername57{othername57:linha.othername57})

                WITH linha WHERE NOT linha.othername58 IS null
                CREATE (other58:othername58{othername58:linha.othername58})

                WITH linha WHERE NOT linha.othername59 IS null
                CREATE (other59:othername59{othername59:linha.othername59})
                
                WITH linha WHERE NOT linha.othername60 IS null
                CREATE (other60:othername60{othername60:linha.othername60})

                WITH linha WHERE NOT linha.othername61 IS null
                CREATE (other61:othername61{othername61:linha.othername61})

                WITH linha WHERE NOT linha.othername62 IS null
                CREATE (other62:othername62{othername62:linha.othername62})

                WITH linha WHERE NOT linha.othername63 IS null
                CREATE (other63:othername63{othername63:linha.othername63})

                WITH linha WHERE NOT linha.othername64 IS null
                CREATE (other64:othername64{othername64:linha.othername64})

                WITH linha WHERE NOT linha.othername65 IS null
                CREATE (other65:othername65{othername65:linha.othername65})

                WITH linha WHERE NOT linha.othername66 IS null
                CREATE (other66:othername66{othername66:linha.othername66})

                WITH linha WHERE NOT linha.othername67 IS null
                CREATE (other67:othername67{othername67:linha.othername67})

                WITH linha WHERE NOT linha.othername68 IS null
                CREATE (other68:othername68{othername68:linha.othername68})

                WITH linha WHERE NOT linha.othername69 IS null
                CREATE (other69:othername69{othername69:linha.othername69})

                WITH linha WHERE NOT linha.othername70 IS null
                CREATE (other70:othername70{othername70:linha.othername70})

                WITH linha WHERE NOT linha.othername71 IS null
                CREATE (other71:othername71{othername71:linha.othername71})
                
                WITH linha WHERE NOT linha.othername72 IS null
                CREATE (other72:othername72{othername72:linha.othername72})

                WITH linha WHERE NOT linha.othername73 IS null
                CREATE (other73:othername73{othername73:linha.othername73})

                WITH linha WHERE NOT linha.othername74 IS null
                CREATE (other74:othername74{othername74:linha.othername74})

                WITH linha WHERE NOT linha.othername75 IS null
                CREATE (other75:othername75{othername75:linha.othername75})

                WITH linha WHERE NOT linha.othername76 IS null
                CREATE (other76:othername76{othername76:linha.othername76})

                WITH linha WHERE NOT linha.othername77 IS null
                CREATE (other77:othername77{othername77:linha.othername77})

                WITH linha WHERE NOT linha.othername78 IS null
                CREATE (other78:othername78{othername78:linha.othername78})

                WITH linha WHERE NOT linha.othername79 IS null
                CREATE (other79:othername79{othername79:linha.othername79})

                WITH linha WHERE NOT linha.othername80 IS null
                CREATE (other80:othername80{othername80:linha.othername80})

                WITH linha WHERE NOT linha.othername81 IS null
                CREATE (other81:othername81{othername81:linha.othername81})

                WITH linha WHERE NOT linha.othername82 IS null
                CREATE (other82:othername82{othername82:linha.othername82})

                WITH linha WHERE NOT linha.othername83 IS null
                CREATE (other83:othername83{othername83:linha.othername83})
                
                WITH linha WHERE NOT linha.othername84 IS null
                CREATE (other84:othername84{othername84:linha.othername84})

                WITH linha WHERE NOT linha.othername85 IS null
                CREATE (other85:othername85{othername85:linha.othername85})

                WITH linha WHERE NOT linha.othername86 IS null
                CREATE (other86:othername86{othername86:linha.othername86})

                WITH linha WHERE NOT linha.othername87 IS null
                CREATE (other87:othername87{othername87:linha.othername87})

                WITH linha WHERE NOT linha.othername88 IS null
                CREATE (other88:othername88{othername88:linha.othername88})

                WITH linha WHERE NOT linha.othername89 IS null
                CREATE (other89:othername89{othername89:linha.othername89})

                WITH linha WHERE NOT linha.othername90 IS null
                CREATE (other90:othername90{othername90:linha.othername90})

                WITH linha WHERE NOT linha.othername91 IS null
                CREATE (other91:othername91{othername91:linha.othername91})

                WITH linha WHERE NOT linha.othername92 IS null
                CREATE (other92:othername92{othername92:linha.othername92})

                WITH linha WHERE NOT linha.othername93 IS null
                CREATE (other93:othername93{othername93:linha.othername93})

                WITH linha WHERE NOT linha.othername94 IS null
                CREATE (other94:othername94{othername94:linha.othername94})

                WITH linha WHERE NOT linha.othername95 IS null
                CREATE (other95:othername95{othername95:linha.othername95})
                
                WITH linha WHERE NOT linha.othername96 IS null
                CREATE (other96:othername96{othername96:linha.othername96})

                WITH linha WHERE NOT linha.othername97 IS null
                CREATE (other97:othername97{othername97:linha.othername97})

                WITH linha WHERE NOT linha.othername98 IS null
                CREATE (other98:othername98{othername98:linha.othername98})

                WITH linha WHERE NOT linha.othername99 IS null
                CREATE (other99:othername99{othername99:linha.othername99})

                WITH linha WHERE NOT linha.othername100 IS null
                CREATE (other100:othername100{othername100:linha.othername100})

                WITH linha WHERE NOT linha.othername101 IS null
                CREATE (other101:othername101{othername101:linha.othername101})

                WITH linha WHERE NOT linha.othername102 IS null
                CREATE (other102:othername102{othername102:linha.othername102})

                WITH linha WHERE NOT linha.othername103 IS null
                CREATE (other103:othername103{othername103:linha.othername103})

                WITH linha WHERE NOT linha.othername104 IS null
                CREATE (other104:othername104{othername104:linha.othername104})

                WITH linha WHERE NOT linha.othername105 IS null
                CREATE (other105:othername105{othername105:linha.othername105})

                WITH linha WHERE NOT linha.othername106 IS null
                CREATE (other106:othername106{othername106:linha.othername106})

                WITH linha WHERE NOT linha.othername107 IS null
                CREATE (other107:othername107{othername107:linha.othername107})

                WITH linha WHERE NOT linha.othername108 IS null
                CREATE (other108:othername108{othername108:linha.othername108})

                WITH linha WHERE NOT linha.othername109 IS null
                CREATE (other109:othername109{othername109:linha.othername109})

                WITH linha WHERE NOT linha.othername110 IS null
                CREATE (other110:othername110{othername110:linha.othername110})

                WITH linha WHERE NOT linha.othername111 IS null
                CREATE (other111:othername111{othername111:linha.othername111})
                
                WITH linha WHERE NOT linha.othername112 IS null
                CREATE (other112:othername112{othername112:linha.othername112})

                WITH linha WHERE NOT linha.othername113 IS null
                CREATE (other113:othername113{othername113:linha.othername113})

                WITH linha WHERE NOT linha.othername114 IS null
                CREATE (other114:othername114{othername114:linha.othername114})

                WITH linha WHERE NOT linha.othername115 IS null
                CREATE (other115:othername115{othername115:linha.othername115})

                WITH linha WHERE NOT linha.othername116 IS null
                CREATE (other116:othername116{othername116:linha.othername116})

                WITH linha WHERE NOT linha.othername117 IS null
                CREATE (other117:othername117{othername117:linha.othername117})

                WITH linha WHERE NOT linha.othername118 IS null
                CREATE (other118:othername118{othername118:linha.othername118})

                WITH linha WHERE NOT linha.othername119 IS null
                CREATE (other119:othername119{othername119:linha.othername119})

                WITH linha WHERE NOT linha.othername120 IS null
                CREATE (other120:othername120{othername120:linha.othername120})

                WITH linha WHERE NOT linha.othername121 IS null
                CREATE (other121:othername121{othername121:linha.othername121})

                WITH linha WHERE NOT linha.othername122 IS null
                CREATE (other122:othername122{othername122:linha.othername122})

                WITH linha WHERE NOT linha.othername123 IS null
                CREATE (other123:othername123{othername123:linha.othername123})
                
                WITH linha WHERE NOT linha.othername124 IS null
                CREATE (other124:othername124{othername124:linha.othername124})

                WITH linha WHERE NOT linha.othername125 IS null
                CREATE (other125:othername125{othername125:linha.othername125})

                WITH linha WHERE NOT linha.othername126 IS null
                CREATE (other126:othername126{othername126:linha.othername126})

                WITH linha WHERE NOT linha.othername127 IS null
                CREATE (other127:othername127{othername127:linha.othername127})

                WITH linha WHERE NOT linha.othername128 IS null
                CREATE (other128:othername128{othername128:linha.othername128})

                WITH linha WHERE NOT linha.othername129 IS null
                CREATE (other129:othername129{othername129:linha.othername129})

                WITH linha WHERE NOT linha.othername130 IS null
                CREATE (other130:othername130{othername130:linha.othername130})

                WITH linha WHERE NOT linha.othername131 IS null
                CREATE (other131:othername131{othername131:linha.othername131})

                WITH linha WHERE NOT linha.othername132 IS null
                CREATE (other132:othername132{othername132:linha.othername132})

                WITH linha WHERE NOT linha.othername133 IS null
                CREATE (other133:othername133{othername133:linha.othername133})

                WITH linha WHERE NOT linha.othername134 IS null
                CREATE (other134:othername134{othername134:linha.othername134})

                WITH linha WHERE NOT linha.othername135 IS null
                CREATE (other135:othername135{othername135:linha.othername135})
                
                WITH linha WHERE NOT linha.othername136 IS null
                CREATE (other136:othername136{othername136:linha.othername136})

                WITH linha WHERE NOT linha.othername137 IS null
                CREATE (other137:othername137{othername137:linha.othername137})

                WITH linha WHERE NOT linha.othername138 IS null
                CREATE (other138:othername138{othername138:linha.othername138})

                WITH linha WHERE NOT linha.othername139 IS null
                CREATE (other139:othername139{othername139:linha.othername139})

                WITH linha WHERE NOT linha.othername140 IS null
                CREATE (other140:othername140{othername140:linha.othername140})

                WITH linha WHERE NOT linha.othername141 IS null
                CREATE (other:othername141{othername141:linha.othername141})

                WITH linha WHERE NOT linha.othername142 IS null
                CREATE (other142:othername142{othername142:linha.othername142})

                WITH linha WHERE NOT linha.othername143 IS null
                CREATE (other143:othername143{othername143:linha.othername143})

                WITH linha WHERE NOT linha.othername144 IS null
                CREATE (other144:othername144{othername144:linha.othername144})

                WITH linha WHERE NOT linha.othername145 IS null
                CREATE (other145:othername145{othername145:linha.othername145})

                WITH linha WHERE NOT linha.othername146 IS null
                CREATE (other146:othername146{othername146:linha.othername146})

                WITH linha WHERE NOT linha.othername147 IS null
                CREATE (other147:othername147{othername147:linha.othername147})
                
                WITH linha WHERE NOT linha.othername148 IS null
                CREATE (other148:othername148{othername148:linha.othername148})

                WITH linha WHERE NOT linha.othername149 IS null
                CREATE (other149:othername149{othername149:linha.othername149})

                WITH linha WHERE NOT linha.othername150 IS null
                CREATE (other150:othername150{othername150:linha.othername150})

                WITH linha WHERE NOT linha.othername151 IS null
                CREATE (other151:othername151{othername151:linha.othername151})

                WITH linha WHERE NOT linha.othername152 IS null
                CREATE (other152:othername152{othername152:linha.othername152})

                WITH linha WHERE NOT linha.othername153 IS null
                CREATE (other153:othername153{othername153:linha.othername153})

                WITH linha WHERE NOT linha.othername154 IS null
                CREATE (other154:othername154{othername154:linha.othername154})

                WITH linha WHERE NOT linha.othername155 IS null
                CREATE (other155:othername155{othername155:linha.othername155})

                WITH linha WHERE NOT linha.othername156 IS null
                CREATE (other156:othername156{othername156:linha.othername156})

                WITH linha WHERE NOT linha.othername157 IS null
                CREATE (other157:othername157{othername157:linha.othername157})

                WITH linha WHERE NOT linha.othername158 IS null
                CREATE (other158:othername158{othername158:linha.othername158})

                WITH linha WHERE NOT linha.othername159 IS null
                CREATE (other159:othername159{othername159:linha.othername159})
                
                WITH linha WHERE NOT linha.othername160 IS null
                CREATE (other160:othername160{othername160:linha.othername160})

                WITH linha WHERE NOT linha.othername161 IS null
                CREATE (other161:othername161{othername161:linha.othername161})

                WITH linha WHERE NOT linha.othername162 IS null
                CREATE (other162:othername162{othername162:linha.othername162})

                WITH linha WHERE NOT linha.othername163 IS null
                CREATE (other163:othername163{othername163:linha.othername163})

                WITH linha WHERE NOT linha.othername164 IS null
                CREATE (other164:othername164{othername164:linha.othername164})

                WITH linha WHERE NOT linha.othername165 IS null
                CREATE (other165:othername165{othername165:linha.othername165})

                WITH linha WHERE NOT linha.othername166 IS null
                CREATE (other166:othername166{othername166:linha.othername166})"""

cqlCreate2= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other0:othername0{othername0:linha.othername0})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other0)-[:OTHER_NAME0]->(Br)

                return *;"""

cqlCreate3= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other1:othername1{othername1:linha.othername1})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other1)-[:OTHER_NAME1]->(Br)

                return *;"""

cqlCreate4= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other2:othername2{othername2:linha.othername2})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other2)-[:OTHER_NAME2]->(Br)

                return *;"""

cqlCreate5= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other3:othername3{othername3:linha.othername3})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other3)-[:OTHER_NAME3]->(Br)

                return *;"""

cqlCreate6= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other4:othername4{othername4:linha.othername4})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other4)-[:OTHER_NAME4]->(Br)

                return *;"""

cqlCreate7= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other5:othername5{othername5:linha.othername5})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other5)-[:OTHER_NAME5]->(Br)

                return *;"""

cqlCreate8= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other6:othername6{othername6:linha.othername6})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other6)-[:OTHER_NAME6]->(Br)

                return *;"""

cqlCreate9= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other7:othername7{othername7:linha.othername7})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other7)-[:OTHER_NAME7]->(Br)

                return *;"""

cqlCreate10= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other8:othername8{othername8:linha.othername8})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other8)-[:OTHER_NAME8]->(Br)

                return *;"""

cqlCreate11= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other9:othername9{othername9:linha.othername9})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other9)-[:OTHER_NAME9]->(Br)

                return *;"""

cqlCreate12= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other10:othername10{othername10:linha.othername10})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other10)-[:OTHER_NAME10]->(Br)

                return *;"""

cqlCreate13= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other11:othername11{othername11:linha.othername11})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other11)-[:OTHER_NAME11]->(Br)

                return *;"""

cqlCreate14= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other12:othername12{othername12:linha.othername12})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other12)-[:OTHER_NAME12]->(Br)

                return *;"""

cqlCreate15= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other13:othername13{othername13:linha.othername13})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other13)-[:OTHER_NAME13]->(Br)

                return *;"""

cqlCreate16= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other14:othername14{othername14:linha.othername14})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other14)-[:OTHER_NAME14]->(Br)

                return *;"""

cqlCreate17= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other15:othername15{othername15:linha.othername15})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other15)-[:OTHER_NAME15]->(Br)

                return *;"""

cqlCreate18= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other16:othername16{othername16:linha.othername16})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other16)-[:OTHER_NAME16]->(Br)

                return *;"""

cqlCreate19= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other17:othername17{othername17:linha.othername17})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other17)-[:OTHER_NAME17]->(Br)

                return *;"""

cqlCreate20= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other18:othername18{othername18:linha.othername18})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other18)-[:OTHER_NAME18]->(Br)

                return *;"""

cqlCreate21= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other19:othername19{othername19:linha.othername19})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other19)-[:OTHER_NAME19]->(Br)

                return *;"""

cqlCreate22= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other20:othername20{othername20:linha.othername20})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other20)-[:OTHER_NAME20]->(Br)

                return *;"""

cqlCreate23= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other21:othername21{othername21:linha.othername21})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other21)-[:OTHER_NAME21]->(Br)

                return *;"""

cqlCreate24= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other22:othername22{othername22:linha.othername22})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other22)-[:OTHER_NAME22]->(Br)

                return *;"""

cqlCreate25= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other23:othername23{othername23:linha.othername23})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other23)-[:OTHER_NAME23]->(Br)

                return *;"""

cqlCreate26= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other24:othername24{othername24:linha.othername24})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other24)-[:OTHER_NAME24]->(Br)

                return *;"""

cqlCreate27= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other25:othername25{othername25:linha.othername25})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other25)-[:OTHER_NAME25]->(Br)

                return *;"""

cqlCreate28= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other26:othername26{othername26:linha.othername26})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other26)-[:OTHER_NAME26]->(Br)

                return *;"""

cqlCreate29= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other27:othername27{othername27:linha.othername27})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other27)-[:OTHER_NAME27]->(Br)

                return *;"""

cqlCreate30= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other28:othername28{othername28:linha.othername28})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other28)-[:OTHER_NAME28]->(Br)

                return *;"""

cqlCreate31= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other29:othername29{othername29:linha.othername29})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other29)-[:OTHER_NAME29]->(Br)

                return *;"""

cqlCreate32= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other30:othername30{othername30:linha.othername30})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other30)-[:OTHER_NAME30]->(Br)

                return *;"""

cqlCreate33= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other31:othername31{othername31:linha.othername31})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other31)-[:OTHER_NAME31]->(Br)

                return *;"""

cqlCreate34= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other32:othername32{othername32:linha.othername32})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other32)-[:OTHER_NAME32]->(Br)

                return *;"""

cqlCreate35= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other33:othername33{othername33:linha.othername33})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other33)-[:OTHER_NAME33]->(Br)

                return *;"""

cqlCreate36= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other34:othername34{othername34:linha.othername34})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other34)-[:OTHER_NAME34]->(Br)

                return *;"""

cqlCreate37= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other35:othername35{othername35:linha.othername35})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other35)-[:OTHER_NAME35]->(Br)

                return *;"""

cqlCreate38= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other36:othername36{othername36:linha.othername36})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other36)-[:OTHER_NAME36]->(Br)

                return *;"""

cqlCreate39= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other37:othername37{othername37:linha.othername37})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other37)-[:OTHER_NAME37]->(Br)

                return *;"""

cqlCreate40= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other38:othername38{othername38:linha.othername38})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other38)-[:OTHER_NAME38]->(Br)

                return *;"""

cqlCreate41= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other39:othername39{othername39:linha.othername39})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other39)-[:OTHER_NAME39]->(Br)

                return *;"""

cqlCreate42= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other40:othername40{othername40:linha.othername40})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other40)-[:OTHER_NAME40]->(Br)

                return *;"""

cqlCreate43= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other41:othername41{othername41:linha.othername41})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other41)-[:OTHER_NAME41]->(Br)

                return *;"""

cqlCreate44= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other42:othername42{othername42:linha.othername42})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other42)-[:OTHER_NAME42]->(Br)

                return *;"""

cqlCreate45= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other43:othername43{othername43:linha.othername43})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other43)-[:OTHER_NAME43]->(Br)

                return *;"""

cqlCreate46= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other44:othername44{othername44:linha.othername44})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other44)-[:OTHER_NAME44]->(Br)

                return *;"""

cqlCreate47= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other45:othername45{othername45:linha.othername45})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other45)-[:OTHER_NAME45]->(Br)

                return *;"""

cqlCreate48= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other46:othername46{othername46:linha.othername46})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other46)-[:OTHER_NAME46]->(Br)

                return *;"""

cqlCreate49= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other47:othername47{othername47:linha.othername47})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other47)-[:OTHER_NAME47]->(Br)

                return *;"""

cqlCreate50= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other48:othername48{othername48:linha.othername48})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other48)-[:OTHER_NAME48]->(Br)

                return *;"""

cqlCreate51= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other49:othername49{othername49:linha.othername49})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other49)-[:OTHER_NAME49]->(Br)

                return *;"""

cqlCreate52= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other50:othername50{othername50:linha.othername50})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other50)-[:OTHER_NAME50]->(Br)
                
                RETURN *;"""

cqlCreate60= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other58:othername58{othername58:linha.othername58})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other58)-[:OTHER_NAME58]->(Br)

                return *;"""

cqlCreate61= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other59:othername59{othername59:linha.othername59})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other59)-[:OTHER_NAME59]->(Br)

                return *;"""

cqlCreate62= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other60:othername60{othername60:linha.othername60})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other60)-[:OTHER_NAME60]->(Br)

                return *;"""

cqlCreate63= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other61:othername61{othername61:linha.othername61})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other61)-[:OTHER_NAME61]->(Br)

                return *;"""

cqlCreate64= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other62:othername62{othername62:linha.othername62})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other62)-[:OTHER_NAME62]->(Br)

                return *;"""

cqlCreate65= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other63:othername63{othername63:linha.othername63})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other63)-[:OTHER_NAME63]->(Br)

                return *;"""

cqlCreate66= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other64:othername64{othername64:linha.othername64})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other64)-[:OTHER_NAME64]->(Br)

                return *;"""

cqlCreate67= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other65:othername65{othername65:linha.othername65})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other65)-[:OTHER_NAME65]->(Br)

                return *;"""

cqlCreate68= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other66:othername66{othername66:linha.othername66})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other66)-[:OTHER_NAME66]->(Br)

                return *;"""

cqlCreate69= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other67:othername67{othername67:linha.othername67})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other67)-[:OTHER_NAME67]->(Br)

                return *;"""

cqlCreate70= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other68:othername68{othername68:linha.othername68})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other68)-[:OTHER_NAME68]->(Br)

                return *;"""

cqlCreate71= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other69:othername69{othername69:linha.othername69})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other69)-[:OTHER_NAME69]->(Br)

                return *;"""

cqlCreate72= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other70:othername70{othername70:linha.othername70})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other70)-[:OTHER_NAME70]->(Br)

                return *;"""

cqlCreate73= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other71:othername71{othername71:linha.othername71})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other71)-[:OTHER_NAME71]->(Br)

                return *;"""

cqlCreate74= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other72:othername72{othername72:linha.othername72})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other72)-[:OTHER_NAME72]->(Br)

                return *;"""

cqlCreate75= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other73:othername73{othername73:linha.othername73})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other73)-[:OTHER_NAME73]->(Br)

                return *;"""

cqlCreate76= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other74:othername74{othername74:linha.othername74})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other74)-[:OTHER_NAME74]->(Br)

                return *;"""

cqlCreate77= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other75:othername75{othername75:linha.othername75})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other75)-[:OTHER_NAME75]->(Br)

                return *;"""

cqlCreate78= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other76:othername76{othername76:linha.othername76})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other76)-[:OTHER_NAME76]->(Br)

                return *;"""

cqlCreate79= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other77:othername77{othername77:linha.othername77})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other77)-[:OTHER_NAME77]->(Br)

                return *;"""

cqlCreate80= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other78:othername78{othername78:linha.othername78})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other78)-[:OTHER_NAME78]->(Br)

                return *;"""

cqlCreate81= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other79:othername79{othername79:linha.othername79})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other79)-[:OTHER_NAME79]->(Br)

                return *;"""

cqlCreate82= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other80:othername80{othername80:linha.othername80})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other80)-[:OTHER_NAME80]->(Br)

                return *;"""

cqlCreate83= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other81:othername81{othername81:linha.othername81})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other81)-[:OTHER_NAME81]->(Br)

                return *;"""

cqlCreate84= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other82:othername82{othername82:linha.othername82})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other82)-[:OTHER_NAME82]->(Br)

                return *;"""

cqlCreate85= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other83:othername83{othername83:linha.othername83})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other83)-[:OTHER_NAME83]->(Br)

                return *;"""

cqlCreate86= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other84:othername84{othername84:linha.othername84})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other84)-[:OTHER_NAME84]->(Br)

                return *;"""

cqlCreate87= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other85:othername85{othername85:linha.othername85})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other85)-[:OTHER_NAME85]->(Br)

                return *;"""

cqlCreate88= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other86:othername86{othername86:linha.othername86})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other86)-[:OTHER_NAME86]->(Br)

                return *;"""

cqlCreate89= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other87:othername87{othername87:linha.othername87})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other87)-[:OTHER_NAME87]->(Br)

                return *;"""

cqlCreate90= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other88:othername88{othername88:linha.othername88})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other88)-[:OTHER_NAME88]->(Br)

                return *;"""

cqlCreate91= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other89:othername89{othername89:linha.othername89})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other89)-[:OTHER_NAME89]->(Br)

                return *;"""

cqlCreate92= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other90:othername90{othername90:linha.othername90})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other90)-[:OTHER_NAME90]->(Br)

                return *;"""

cqlCreate93= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other91:othername91{othername91:linha.othername91})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other91)-[:OTHER_NAME91]->(Br)

                return *;"""

cqlCreate94= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other92:othername92{othername92:linha.othername92})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other92)-[:OTHER_NAME92]->(Br)

                return *;"""

cqlCreate95= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other93:othername93{othername93:linha.othername93})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other93)-[:OTHER_NAME93]->(Br)

                return *;"""

cqlCreate96= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other94:othername94{othername94:linha.othername94})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other94)-[:OTHER_NAME94]->(Br)

                return *;"""

cqlCreate97= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other95:othername95{othername95:linha.othername95})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other95)-[:OTHER_NAME95]->(Br)

                return *;"""

cqlCreate98= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other96:othername96{othername96:linha.othername96})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other96)-[:OTHER_NAME96]->(Br)

                return *;"""

cqlCreate99= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other97:othername97{othername97:linha.othername97})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other97)-[:OTHER_NAME97]->(Br)

                return *;"""

cqlCreate100= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other98:othername98{othername98:linha.othername98})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other98)-[:OTHER_NAME98]->(Br)

                return *;"""

cqlCreate101= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other99:othername99{othername99:linha.othername99})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other99)-[:OTHER_NAME99]->(Br)

                return *;"""

cqlCreate102= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other100:othername100{othername100:linha.othername100})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other100)-[:OTHER_NAME100]->(Br)

                return *;"""

cqlCreate103= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other101:othername101{othername101:linha.othername101})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other101)-[:OTHER_NAME101]->(Br)

                return *;"""

cqlCreate104= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other102:othername102{othername102:linha.othername102})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other102)-[:OTHER_NAME102]->(Br)

                return *;"""

cqlCreate105= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other103:othername103{othername103:linha.othername103})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other103)-[:OTHER_NAME103]->(Br)

                return *;"""

cqlCreate106= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other104:othername104{othername104:linha.othername104})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other104)-[:OTHER_NAME104]->(Br)

                return *;"""

cqlCreate107= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other105:othername105{othername105:linha.othername105})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other105)-[:OTHER_NAME105]->(Br)

                return *;"""

cqlCreate108= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other106:othername106{othername106:linha.othername106})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other106)-[:OTHER_NAME106]->(Br)

                return *;"""

cqlCreate109= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other107:othername107{othername107:linha.othername107})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other107)-[:OTHER_NAME107]->(Br)

                return *;"""

cqlCreate110= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other108:othername108{othername108:linha.othername108})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other108)-[:OTHER_NAME108]->(Br)

                return *;"""

cqlCreate111= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other109:othername109{othername109:linha.othername109})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other109)-[:OTHER_NAME109]->(Br)

                return *;"""

cqlCreate112= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other110:othername110{othername110:linha.othername110})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other110)-[:OTHER_NAME110]->(Br)

                return *;"""

cqlCreate113= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other111:othername111{othername111:linha.othername111})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other111)-[:OTHER_NAME111]->(Br)

                return *;"""

cqlCreate114= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other112:othername112{othername112:linha.othername112})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other112)-[:OTHER_NAME112]->(Br)

                return *;"""

cqlCreate115= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other113:othername113{othername113:linha.othername113})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other113)-[:OTHER_NAME113]->(Br)

                return *;"""

cqlCreate116= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other114:othername114{othername114:linha.othername114})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other114)-[:OTHER_NAME114]->(Br)

                return *;"""

cqlCreate117= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other115:othername115{othername115:linha.othername115})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other115)-[:OTHER_NAME115]->(Br)

                return *;"""

cqlCreate118= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other116:othername116{othername116:linha.othername116})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other116)-[:OTHER_NAME116]->(Br)

                return *;"""

cqlCreate119= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other117:othername117{othername117:linha.othername117})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other117)-[:OTHER_NAME117]->(Br)

                return *;"""

cqlCreate120= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other118:othername118{othername118:linha.othername118})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other118)-[:OTHER_NAME118]->(Br)

                return *;"""

cqlCreate121= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other119:othername119{othername119:linha.othername119})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other119)-[:OTHER_NAME119]->(Br)

                return *;"""

cqlCreate122= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other120:othername120{othername120:linha.othername120})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other120)-[:OTHER_NAME120]->(Br)

                return *;"""

cqlCreate123= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other121:othername121{othername121:linha.othername121})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other121)-[:OTHER_NAME121]->(Br)

                return *;"""

cqlCreate124= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other122:othername122{othername122:linha.othername122})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other122)-[:OTHER_NAME122]->(Br)

                return *;"""

cqlCreate125= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other123:othername123{othername123:linha.othername123})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other123)-[:OTHER_NAME123]->(Br)

                return *;"""

cqlCreate126= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other124:othername124{othername124:linha.othername124})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other124)-[:OTHER_NAME124]->(Br)

                return *;"""

cqlCreate127= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other125:othername125{othername125:linha.othername125})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other125)-[:OTHER_NAME125]->(Br)

                return *;"""

cqlCreate128= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other126:othername126{othername126:linha.othername126})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other126)-[:OTHER_NAME126]->(Br)

                return *;"""

cqlCreate129= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other127:othername127{othername127:linha.othername127})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other127)-[:OTHER_NAME127]->(Br)

                return *;"""

cqlCreate130= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other128:othername128{othername128:linha.othername128})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other128)-[:OTHER_NAME128]->(Br)

                return *;"""

cqlCreate131= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other129:othername129{othername129:linha.othername129})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other129)-[:OTHER_NAME129]->(Br)

                return *;"""

cqlCreate132= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other130:othername130{othername130:linha.othername130})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other130)-[:OTHER_NAME130]->(Br)

                return *;"""

cqlCreate133= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other131:othername131{othername131:linha.othername131})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other131)-[:OTHER_NAME131]->(Br)

                return *;"""

cqlCreate134= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other132:othername132{othername132:linha.othername132})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other132)-[:OTHER_NAME132]->(Br)

                return *;"""

cqlCreate135= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other133:othername133{othername133:linha.othername133})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other133)-[:OTHER_NAME133]->(Br)

                return *;"""

cqlCreate136= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other134:othername134{othername134:linha.othername134})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other134)-[:OTHER_NAME134]->(Br)

                return *;"""

cqlCreate137= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other135:othername135{othername135:linha.othername135})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other135)-[:OTHER_NAME135]->(Br)

                return *;"""

cqlCreate138= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other136:othername136{othername136:linha.othername136})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other136)-[:OTHER_NAME136]->(Br)

                return *;"""

cqlCreate139= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other137:othername137{othername137:linha.othername137})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other137)-[:OTHER_NAME137]->(Br)

                return *;"""

cqlCreate140= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other138:othername138{othername138:linha.othername138})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other138)-[:OTHER_NAME138]->(Br)

                return *;"""

cqlCreate141= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other139:othername139{othername139:linha.othername139})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other139)-[:OTHER_NAME139]->(Br)

                return *;"""

cqlCreate142= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other140:othername140{othername140:linha.othername140})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other140)-[:OTHER_NAME140]->(Br)

                return *;"""

cqlCreate143= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other141:othername141{othername141:linha.othername141})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other141)-[:OTHER_NAME141]->(Br)

                return *;"""

cqlCreate144= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other142:othername142{othername142:linha.othername142})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other142)-[:OTHER_NAME142]->(Br)

                return *;"""

cqlCreate145= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other143:othername143{othername143:linha.othername143})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other143)-[:OTHER_NAME143]->(Br)

                return *;"""

cqlCreate146= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other144:othername144{othername144:linha.othername144})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other144)-[:OTHER_NAME144]->(Br)

                return *;"""

cqlCreate147= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other145:othername145{othername145:linha.othername145})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other145)-[:OTHER_NAME145]->(Br)

                return *;"""

cqlCreate148= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other146:othername146{othername146:linha.othername146})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other146)-[:OTHER_NAME146]->(Br)

                return *;"""

cqlCreate149= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other147:othername147{othername147:linha.othername147})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other147)-[:OTHER_NAME147]->(Br)

                return *;"""

cqlCreate150= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other148:othername148{othername148:linha.othername148})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other148)-[:OTHER_NAME148]->(Br)

                return *;"""

cqlCreate151= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other149:othername149{othername149:linha.othername149})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other149)-[:OTHER_NAME149]->(Br)

                return *;"""

cqlCreate152= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other150:othername150{othername150:linha.othername150})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other150)-[:OTHER_NAME150]->(Br)

                return *;"""

cqlCreate153= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other151:othername151{othername151:linha.othername151})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other151)-[:OTHER_NAME151]->(Br)

                return *;"""

cqlCreate154= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other152:othername152{othername152:linha.othername152})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other152)-[:OTHER_NAME152]->(Br)

                return *;"""

cqlCreate155= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other153:othername153{othername153:linha.othername153})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other153)-[:OTHER_NAME153]->(Br)

                return *;"""

cqlCreate156= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other154:othername154{othername154:linha.othername154})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other154)-[:OTHER_NAME154]->(Br)

                return *;"""

cqlCreate157= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other155:othername155{othername155:linha.othername155})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other155)-[:OTHER_NAME155]->(Br)

                return *;"""

cqlCreate158= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other156:othername156{othername156:linha.othername156})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other156)-[:OTHER_NAME156]->(Br)

                return *;"""

cqlCreate159= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other157:othername157{othername157:linha.othername157})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other157)-[:OTHER_NAME157]->(Br)

                return *;"""

cqlCreate160= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other158:othername158{othername158:linha.othername158})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other158)-[:OTHER_NAME158]->(Br)

                return *;"""

cqlCreate161= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other159:othername159{othername159:linha.othername159})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other159)-[:OTHER_NAME159]->(Br)

                return *;"""

cqlCreate162= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other160:othername160{othername160:linha.othername160})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other160)-[:OTHER_NAME160]->(Br)

                return *;"""

cqlCreate163= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other161:othername161{othername161:linha.othername161})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other161)-[:OTHER_NAME161]->(Br)

                return *;"""

cqlCreate164= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other162:othername162{othername162:linha.othername162})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other162)-[:OTHER_NAME162]->(Br)

                return *;"""

cqlCreate165= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other163:othername163{othername163:linha.othername163})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other163)-[:OTHER_NAME163]->(Br)

                return *;"""

cqlCreate166= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other164:othername164{othername164:linha.othername164})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other164)-[:OTHER_NAME164]->(Br)

                return *;"""

cqlCreate167= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other165:othername165{othername165:linha.othername165})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other165)-[:OTHER_NAME165]->(Br)

                return *;"""

cqlCreate168= """LOAD CSV WITH HEADERS FROM 'file:///OtherNames.csv' AS linha


                MATCH(other166:othername166{othername166:linha.othername166})

                MATCH(Br:BRAZIL{name:linha.name})

                CREATE(other166)-[:OTHER_NAME166]->(Br)

                return *;"""


cqlCreate170 = """LOAD CSV WITH HEADERS FROM file:///OtherNames.csv AS linha

              


               
                """
                
# Função para criar um arquivo csv com os nomes alternativos separados por colunas

def div_names():
    df = pd.read_csv('BR.csv')
    df = df.join(df['alternatenames'].str.split('$', expand=True).add_prefix('othername'))
    print(df)
    df2 = df.drop('alternatenames', axis=1)
    df2.to_csv('OtherNames.csv')
#div_names()

# Criação dos nós
with db.session() as graphDB_Session:
        graphDB_Session.run(cqlCreate)
        graphDB_Session.run(cqlCreate1)
        #graphDB_Session.run(cqlCreate2)
#Query do grafo
    #nodes = graphDB_Session.run(cqlNodeQuery)
