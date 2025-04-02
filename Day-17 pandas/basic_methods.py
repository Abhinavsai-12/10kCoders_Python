import pandas as pd

df = pd.read_csv(r"Day-17 pandas\data.csv")
print(df.head(2))
print(df.tail(2))

print(df.info())
print(df.describe())  #stastistic
print(df.columns)
print(df.index)

