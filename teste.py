from py2neo import Graph
import shapely.wkt
from shapely.wkt import loads
import pandas as pd
from shapely.geometry import Point, Polygon

def create_relatBR_02():
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

                    print(f"Relationship created for {row['name']} with Alagoas")
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

                    print(f"Relationship created for {row['name']} with Maranhão")
                else:
                    print(f"{row['name']} don't match with Maranhão:", point)  

                if paraiba_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraíba" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Paraíba")
                else:
                    print(f"{row['name']} don't match with Paraíba:", point)         

                if pernambuco_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Pernambuco" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Pernambuco")
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

                    print(f"Relationship created for {row['name']} with Rio Grande do Norte")
                else:
                    print(f"{row['name']} don't match with Rio Grande do Norte:", point)  

                if sergipe_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Sergipe" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Sergipe")
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

                    print(f"Relationship created for {row['name']} with Amazonas")
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

                    print(f"Relationship created for {row['name']} with Rondônia")
                else:
                    print(f"{row['name']} don't match with Rondônia:", point) 

                if roraima_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Roraima" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Roraima")
                else:
                    print(f"{row['name']} don't match with Roraima:", point)  

                if tocantins_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Tocantins" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Tocantins")
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

                    print(f"Relationship created for {row['name']} with Espírito Santo")
                else:
                    print(f"{row['name']} don't match with Espírito Santo:", point)

                if minas_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Minas Gerais" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Minas Gerais")
                else:
                    print(f"{row['name']} don't match with Minas Gerais:", point) 

                if sao_paulo_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "São Paulo" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with São Paulo")
                else:
                    print(f"{row['name']} don't match with São Paulo:", point)  

                if rio_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Rio de Janeiro" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Rio de Janeiro")
                else:
                    print(f"{row['name']} don't match with Rio de Janeiro:", point)                                             

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

                    print(f"Relationship created for {row['name']} with Rio Grande do Sul")
                else:
                    print(f"{row['name']} don't match with Rio Grande do Sul:", point)    

                if parana_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Paraná" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Paraná")
                else:
                    print(f"{row['name']} don't match with Paraná:", point)    

                if santa_catarina_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Santa Catarina" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Santa Catarina")
                else:
                    print(f"{row['name']} don't match with Santa Catarina:", point)                                           

            else:
                print(f"{row['name']} don't match with Sul:", point)


            if centro_oeste_polygon.contains(point):
                # If the point is inside the polygon, create a relationship in Neo4j
                query = f'MATCH(r:REGIONS), (l:LOCATIONS) WHERE r.name = "Centro-Oeste" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_REGION]->(r)'
                graph.run(query)

                print(f"Relationship created for {row['name']} with Centro-Oeste")

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

                    print(f"Relationship created for {row['name']} with Mato Grosso do Sul")
                else:
                    print(f"{row['name']} don't match with Mato Grosso do Sul:", point) 

                if mato_grosso_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Mato Grosso" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Mato Grosso")
                else:
                    print(f"{row['name']} don't match with Mato Grosso:", point)  

                if distrito_federal_polygon.contains(point):
                    # If the point is inside the polygon, create a relationship in Neo4j
                    query = f'MATCH(s:STATES), (l:LOCATIONS) WHERE s.name = "Distrito Federal" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN_STATE]->(s)'
                    graph.run(query)

                    print(f"Relationship created for {row['name']} with Distrito Federal")
                else:
                    print(f"{row['name']} don't match with Distrito Federal:", point)                                                               

            else:
                print(f"{row['name']} don't match with Centro-Oeste:", point)
        else:
            print(f"{row['name']} don't match with Brazil:", point)

create_relatBR_02()
