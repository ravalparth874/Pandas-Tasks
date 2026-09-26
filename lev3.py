import pandas as pd

df = pd.read_csv("data.csv")
print(df)

# 24
students = df[df["Result"] > 70]
print(students)

# 25
students = df[df["Result"] < 50]
print(students)

# 26
students = df[df["Result"].between(50,80)]
print(students)

# 27
students = df[df["ComingMethod"] == "Cycle"]
print(students)

# 28
students = df[df["ComingMethod"] == "Bus"]
print(students)

# 29
students = df[df["City"] == "Surat"]
print(students)

# 30 
students = df[df["FavSub"] == "Maths"]
print(students)

# 31 
students = df[(df["City"] == "Surat") & (df["ComingMethod"] == "Cycle")]
print(students)

# 32
students = df[(df["FavSub"] == "Science") & (df["Result"] > 70)]
print(students)

# 33 
students = df[(df["ComingMethod"] == "Walk") | (df["Result"] < 70)]
print(students)