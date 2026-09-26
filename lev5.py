import pandas as pd

df = pd.read_csv("data.csv")

# 46
print(df["FavSub"].value_counts())

# 47
print(df["ComingMethod"].value_counts())

# 48
print(df["City"].value_counts())

# 49
print(df.groupby("FavSub")["Result"].mean())

# 50
print(df.groupby("City")["Result"].mean())

# 51
print(df.groupby("ComingMethod")["Result"].mean())

# 52
print(df.groupby("FavSub")["Result"].max())

# 53
print(df.groupby("City")["Result"].min())

# 54
df1 = df.groupby("FavSub")["Result"].mean()
print(df1.idxmax())

# 55
df2 = df.groupby("City")["Result"].mean()
print(df2.idxmax())