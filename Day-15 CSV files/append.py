import csv  # Make sure to import the CSV module

with open("data1.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sophia", 27, "Toronto"])
