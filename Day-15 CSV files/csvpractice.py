import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)  # Read file
    for row in reader:
        print(row)  # Each row is a list
print(reader)