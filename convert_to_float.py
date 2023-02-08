import csv

# List to store the CSV data
csv_data = []

# Read CSV data into the list
with open("OtherNames.csv", "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_data.append(row)

# Convert the specified column from string to float
column_index = 4  # The index of the column to be converted (0-based)
for row in csv_data:
    row[4] = float(row[4])

column_index = 5  # The index of the column to be converted (0-based)
for row in csv_data:
    row[5] = float(row[5])

# Write the updated data to a new CSV file
with open("OtherNamesConverted.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)