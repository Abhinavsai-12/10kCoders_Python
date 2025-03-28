import csv

with open("data2.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")  # Change delimiter
    for row in reader:
        print(row)
