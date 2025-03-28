import csv

data = [
    {"Name": "Joe", "Age": 35, "City": "Chicago"},
    {"Name": "Ane", "Age": 28, "City": "Los Angeles"}
]

with open("data2.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write header
    writer.writerows(data)  # Write multiple rows
