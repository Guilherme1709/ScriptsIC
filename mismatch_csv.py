import shapely.wkt
from shapely.wkt import loads
from shapely.geometry import Point
import pandas as pd

# Read CSV data into the list
df = pd.read_csv('OtherNames_12.csv')

# Read WKT data from file
with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wktfile:
    wkt_data = shapely.wkt.loads(wktfile.read())

#Empty dataframe to hold mismatch coordinates
mismatch = pd.DataFrame(columns=df.columns)

# Check the coordinates between the CSV and WKT data
for i, row in df.iterrows():
     # Extract latitude and longitude values from the CSV data
    latitude = row["latitude"]
    longitude = row["longitude"]

    # Create a shapely Point object from the coordinates
    point = Point(longitude, latitude)
    if not wkt_data.contains(point):
        mismatch = pd.concat([mismatch, row.to_frame().transpose()])
        print("The following coordinates don't match", i+1, ":", point)

    else: 
        print('ok', i+1, "", point)

print("Total de coordenadas inconsistentes: ", len(mismatch))
mismatch.to_csv('mismatch_coordinates12.csv', index=False)