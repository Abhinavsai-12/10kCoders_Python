import os
import csv

filename = "output.csv"

if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])  # Write header
