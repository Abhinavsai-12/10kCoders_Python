import csv

data = [
    ["Name", "Age", "City"],
    ["Sophia", 27, "Toronto"],
    ["John", 30, "New York"]
]

with open("data2.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")  # Use '|' as delimiter
    writer.writerows(data)
