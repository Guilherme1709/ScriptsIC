import csv
import shapely.wkt
import pandas as pd

# List to store the CSV data
csv_data = []

# Read CSV data into the list
with open("OtherNames_0.csv", "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_data.append(row)

# Read WKT data from file
with open("C:\\Users\\guilh\\OneDrive\\Documentos\\Faculdade\\Períodos\\IC - Gazetteer\\scriptspython\\WKT_files\\sudeste\\sudeste.wkt", "r") as wktfile:
    wkt_data = shapely.wkt.loads(wktfile.read())


# Check the coordinates between the CSV and WKT data
for i, row in enumerate(csv_data):
    csv_coord = (float(row[5]), float(row[4]))
    if not wkt_data.contains(shapely.geometry.Point(*csv_coord)):
        print("The following coordinates don't match", i+1, ":", csv_coord)
