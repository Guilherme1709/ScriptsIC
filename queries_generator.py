def comandos():
    i = 0
    for i in range(167):
        print('cqlCreate'+str(i)+'= """LOAD CSV WITH HEADERS FROM \'file:///OtherNames.csv\' AS linha\n\n')
        print('\t\tMATCH(other'+str(i)+':othername'+str(i)+'{othername'+str(i)+':linha.othername'+str(i)+'})\n')
        print('\t\tMATCH(Br:BRAZIL{name:linha.name})\n')
        print('\t\tCREATE(other'+str(i)+')-[:OTHER_NAME'+str(i)+']->(Br)\n')
        print(('\t\treturn *;"""\n'))
#comandos()

def run():
    for i in range(155):
        print('\tgraphDB_Session.run(cqlCreate'+str(i+15)+')')
#run()

def relations():
    i = 0
    for i in range(13):
        print('cqlCreate'+str(i)+'= """LOAD CSV WITH HEADERS FROM ''''file:///OtherNames_'''+str(i)+'.csv'' AS linha\n\n')
        print('\t\tMATCH(other'+str(i)+':othername'+str(i)+'{othername'+str(i)+':linha.othername'+str(i)+'})\n')
        print('\t\tMATCH(Br:BRAZIL{name:linha.name})\n')
        print('WHERE other'+str(i)+'.geonameid = Br.geonameid')
        print('\t\tCREATE(other'+str(i)+')-[:OTHER_NAME'+str(i)+']->(Br)\n')
        print(('\t\treturn *;"""\n'))

#relations()

def index():
    i = 0
    for i in range(67):
        print('cqlCreate0'+str(i)+' = """create index other'+str(i)+'_index for (o'+str(i)+':othername'+str(i)+') on (o'+str(i)+'.othername'+str(i)+');"""')
#index()

def rel():
    i = 0
    for i in range(13):
        print('cqlCreate'+str(i)+' = """LOAD CSV WITH HEADERS FROM ''''file:///OtherNames_'''+str(i)+'.csv'' AS linha\n')

        print("""\t\tCREATE (Br:BRAZIL {elevation:linha.elevation, featurecode:linha.featurecode,
                geonameid:linha.geonameid, timezone:linha.timezone, latitude:linha.latitude,
                dem:linha.dem, admin2code:linha.admin2code, population:linha.population,
                featureclass:linha.featureclass, cc2:linha.cc2,
                admin3code:linha.admin3code, name:linha.name, admin1code:linha.admin1code,
                countrycode:linha.countrycode, admin4code:linha.admin4code, \n\t\tmodificationdate:linha.modificationdate, longitude:linha.longitude})""")

        print("""\n\t\tWITH linha WHERE NOT linha.asciiname IS null""")
        print('\t\tCREATE (ascii:ASCIINAME{asciiname: linha.asciiname, geonameid:linha.geonameid})\n')

        print('\t\tWITH linha WHERE NOT linha.othername0 IS null')
        print('\t\tCREATE (other0:othername0{othername0:linha.othername0, geonameid:linha.geonameid})"""')

        print('\n\ncqlCreate'+str(i)+' = """LOAD CSV WITH HEADERS FROM ''''file:///OtherNames_'''+str(i)+'.csv'' AS linha\n\n')
        print('\t\tMATCH(other0:othername0{othername0:linha.othername})\n')
        print('\t\tMATCH(Br:BRAZIL{name:linha.name})\n')
        print('\t\tWHERE other'+str(i)+'.geonameid = Br.geonameid')
        print('\t\tCREATE(other0)-[:OTHER_NAME0]->(Br)\n')
        print(('\t\treturn *;"""\n'))

#rel()

def dep():
    i = 0
    for i in range(67):
        print('\n\ncqlCreate'+str(i+604)+' = """LOAD CSV WITH HEADERS FROM '+"""'file:///OtherNames_11.csv'"""+' AS linha\n\n')
        print('\t\tMATCH(other'+str(i)+':othername'+str(i)+'{othername'+str(i)+':linha.othername'+str(i)+'})')
        print('\t\tMATCH(Br:BRAZIL{name:linha.name})')
        print('\t\tWHERE other'+str(i)+'.geonameid = Br.geonameid')
        print('\t\tMERGE(other'+str(i)+')-[r'+str(i)+':OTHER_NAME'+str(i)+']->(Br)\n')
        print(('\t\treturn r'+str(i)+';"""\n'))
#dep()

def runing():
    i = 0
    for i in range(69):
        print('graphDB_Session.run(cqlCreate0'+str(i)+')')
#runing()


def regions():
    i = 0
    for i in range(13):
        print('def create_relatBR_'+str(i)+'():')

        print('#Read CSV data')
        print('\tdf = pd.read_csv("OtherNames_'+str(i)+'.csv")')

        print('# Read WKT data from file')
        print('\twith open("C:'+chr(92)+chr(92)+'Users'+chr(92)+chr(92)+'guilh'+chr(92)+chr(92)+'OneDrive'+chr(92)+chr(92)+'Documentos'+chr(92)+chr(92)+'Faculdade'+chr(92)+chr(92)+'Períodos'+chr(92)+chr(92)+'IC - Gazetteer'+chr(92)+chr(92)+'scriptspython'+chr(92)+chr(92)+'wkt_polygons_bruno'+chr(92)+chr(92)+'brasil.wkt", "r") as wktfile:')
        print('\t\twkt_data = shapely.wkt.loads(wktfile.read())')


        print('# Check the coordinates between the CSV and WKT data')
        print('\t\tfor i, row in df.iterrows():')
        print('\t\t\tcsv_coord = (float(row[5]), float(row[4]))')
        print('\t\t\tif wkt_data.contains(shapely.geometry.Point(*csv_coord)):')
        print('\t\t\t\twith db.session() as graphDB_Session:')
        print('\t\t\t\t\tgraphDB_Session.run(cqlCreate'+str(607+i)+')')
        print('\t\t\t\t\tprint("created'+chr(92)+'n")')
        print('\t\t\telse:\n')
        print('\t\t\t\tprint("The following coordinates do not match", i+1, ":", csv_coord)')
        print('#create_relatBR_'+str(i)+'()\n')

regions()



