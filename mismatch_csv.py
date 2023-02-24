import csv
import shapely.wkt
import pandas as pd

# List to store the CSV data
csv_data = []

# Read CSV data into the list
df = pd.read_csv('OtherNames.csv')

# Read WKT data from file
with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\wkt_polygons_bruno\\brasil.wkt", "r") as wktfile:
    wkt_data = shapely.wkt.loads(wktfile.read())

#Empty dataframe to hold mismatch coordinates
mismatch = pd.DataFrame(columns=df.columns)

# Check the coordinates between the CSV and WKT data
for i, row in df.iterrows():
    csv_coord = (float(row[5]), float(row[4]))
    if not wkt_data.contains(shapely.geometry.Point(*csv_coord)):
        mismatch= pd.concat([mismatch, df])
        print("The following coordinates don't match", i+1, ":", csv_coord)
 
    else:
        print('ok', i+1, "", csv_coord)
        
mismatch.to_csv('mismatch_coordinates.csv', index=False)