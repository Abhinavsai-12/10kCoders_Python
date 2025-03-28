import csv

data = [
    ["Name", "Age", "City"],
    ["David", 28, "Berlin"],
    ["Emma", 24, "Paris"]
]

with open("data1.csv", "w", newline="") as file:
    writer = csv.writer(file)  # Create writer object
    writer.writerows(data)  # Write all rows at once
