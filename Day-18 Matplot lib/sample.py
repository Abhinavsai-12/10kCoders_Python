# import matplotlib
# print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 8, 20, 18]

# plt.plot(x, y)  # Create a line plot
# #plt.show()  # Display the plot
# plt.plot(x, y, marker="o", linestyle="--", color="b")

# plt.xlabel("X-axis Label")  # Label for X-axis
# plt.ylabel("Y-axis Label")  # Label for Y-axis
# plt.title("Line Plot Example")  # Title of the Graph
# plt.show()







# import matplotlib.pyplot as plt

# # Sample Data
# x = [1, 2, 3, 4, 5]
# y1 = [10, 20, 25, 30, 40]
# y2 = [5, 15, 20, 25, 35]

# # Create the plot
# plt.plot(x, y1, label="Line 1", color="blue", marker="o")  # First Line
# plt.plot(x, y2, label="Line 2", color="red", linestyle="--", marker="s")  # Second Line

# # Add Title & Labels
# plt.title("Line Plot with Grid & Legend")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# # # Add Grid
# plt.grid(True)  # Show grid lines

# # # Add Legend
# plt.legend()  # Show legend

# # Show the plot
# plt.show()









import matplotlib.pyplot as plt
# categories = ["A", "B", "C", "D"]
# values = [5, 7, 3, 8]

# plt.bar(categories, values, color="green")
# plt.show()

# plt.scatter(categories, values, color="red", marker="x")
# plt.show()







# Histogram chart
# import numpy as np

# data = np.random.randn(1000)  # Random data
# plt.hist(data, bins=20, color="purple", edgecolor="black")
# plt.show()







labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["blue", "red", "green", "yellow"])
plt.title("Pie Chart Example")
plt.show()





