import pandas as pd

df = pd.read_csv("data.csv")

# 35
highest = df["Result"].max()
print(highest)

# 36 
lowest = df["Result"].min()
print(lowest)

# 37
avg = df["Result"].mean()
print(avg)

# 38
avgpd = df["Pd"].mean()
print(avgpd)

# 39
avgpd = df["Pd"].mean()
print(avgpd)

# 40
higheststudent = df.loc[df["Result"].idxmax()]
print(higheststudent)

# 41
loweststudent = df.loc[df["Result"].idxmin()]
print(loweststudent)

# 42
df = df.sort_values("Result", ascending=False)
print(df)

# 43 
df = df.sort_values("Result", ascending=True)
print(df)

# 44
df1 = df.sort_values("Result", ascending=False)
print(df1[0:5])