from py2neo import Graph
import shapely.wkt
from shapely.wkt import loads
import pandas as pd
from shapely.geometry import Point, Polygon

def create_relatBR_0():
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

    # Read CSV data
    df = pd.read_csv("OtherNames_0.csv")

    # Read WKT data from file
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wktfile:
        wkt_data = shapely.wkt.loads(wktfile.read())

    # Check the coordinates between the CSV and WKT data
    for i, row in df.iterrows():
        csv_coord = (float(row[5]), float(row[4]))
        if wkt_data.contains(shapely.geometry.Point(*csv_coord)):
            query = f"""MATCH (location:LOCATIONS {{name: "{row[2]}"}}),
                        (country:BRAZIL {{name: "Brasil"}})
                        MERGE (location)-[isin:IS_IN]->(country)
                        RETURN isin;"""
            graph.run(query)
            print("created\n", ":", csv_coord)
        else:
            print("The following coordinates do not match",
                  i+1, ":", csv_coord)

#create_relatBR_0()

def create_relatBR_02():
    # Load the CSV file with location data
    df = pd.read_csv("OtherNames_0.csv")

    # Load the WKT file with Brazil boundary polygon
    with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wkt_file:
        wkt_data = wkt_file.read()
        brazil_polygon = loads(wkt_data)

    # Connect to Neo4j
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

    mismatch = 0
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
            query = f'MATCH(b:BRAZIL), (l:LOCATIONS) WHERE b.name = "Brasil" and l.latitude = "{row["latitude"]}" and l.longitude = "{row["longitude"]}" MERGE (l)-[isin:IS_IN]->(b)'
            graph.run(query)

            #query = f'LOAD CSV WITH HEADERS FROM "file:///OtherNames_0.csv" AS linha MATCH (b:BRAZIL), (l:LOCATIONS {{name: "{row["name"]}"}}) WHERE b.name = "Brasil" and l.name = linha.name MERGE (l)-[:IS_IN]->(b)'
            #graph.run(query)
            print(f"Created relationship for {row['name']} with Brazil")
        else:
            mismatch += 1
    print("Total of mismatches:", mismatch)
create_relatBR_02()
