def comandos():
    i = 0
    for i in range(90):
        print('cqlCreate'+str(i+92)+'= """LOAD CSV WITH HEADERS FROM \'file:///OtherNames.csv\' AS linha\n\n')
        print('\t\tMATCH(other'+str(i+90)+':othername'+str(i+90)+'{othername'+str(i+90)+':linha.othername'+str(i+90)+'})\n')
        print('\t\tMATCH(Br:BRAZIL{name:linha.name})\n')
        print('\t\tCREATE(other'+str(i+90)+')-[:OTHER_NAME'+str(i+90)+']->(Br)\n')
        print(('\t\treturn *;"""\n'))
comandos()

def run():
    for i in range(155):
        print('\tgraphDB_Session.run(cqlCreate'+str(i+15)+')')
#run()

def relations():
    i = 0
    for i in range(90):
        #print('cqlCreate'+str(i+104)+'= """LOAD CSV WITH HEADERS FROM ''file:///OtherNames.csv'' AS linha\n\n')
        print('\t\tMATCH(other'+str(i+89)+':othername'+str(i+89)+'{othername'+str(i+89)+':linha.othername'+str(i+89)+'})\n')
        #print('\t\tMATCH(Br:BRAZIL{name:linha.name})\n')
        print('\t\tCREATE(other'+str(i+89)+')-[:OTHER_NAME'+str(i+89)+']->(Br)\n')
        #print(('\t\treturn *;"""\n'))

#relations()