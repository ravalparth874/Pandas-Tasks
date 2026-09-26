import pandas as pd

df = pd.read_csv("data.csv")

# 57
highpd = df.loc[df["Pd"].idxmax()]
print(highpd)

# 58
highad = df.loc[df["Ad"].idxmax()]
print(highad)

# 59 
print(df.loc[df["Pd"].idxmin()])

# 60
print(df.loc[df["Pd"] >= 100])

# 61
print(df.loc[df["Ad"] >= 100])

# 62
print(df.loc[df["Pd"] > df["Ad"]])

# 63
print(df.loc[df["Ad"] > df["Pd"]])

# 64
df3 = df.loc[df["ComingMethod"] == "Cycle"]
print(df3["Result"].mean())

# 65
print(df.loc[df["ComingMethod"] == "Bus"]["Result"].mean())

# 66
print(df["City"].value_counts().idxmax())

# 67
print(df["FavSub"].value_counts().idxmax())

# 68
avg_result = df.groupby("ComingMethod")["Result"].mean()
print(avg_result.idxmax())

# 69
highest = df.sort_values("Result", ascending=False)
print(highest.head(3))

# 70
print(df.loc[df.groupby("FavSub")["Result"].idxmax()])

# 71
print(df["Result"].mean())
print(df.loc[df["Result"] >= df["Result"].mean()])