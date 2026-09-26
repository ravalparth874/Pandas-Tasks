import pandas as pd

df = pd.read_csv("data.csv")

# Level 1

# print(df.shape) # to know rows and columns
# print(df.columns)
# print(df.columns.tolist())
# print(len(df))
# print(df.isnull().sum()) #  Column-wise NULL count
# print(df.isnull().sum().sum()) # Entire dataser Null count
# print(df.isnull().sum().idxmax())
# print(df.duplicated().any())

# print(df["FavSub"].unique())
# print(df["ComingMethod"].unique())
# print(df["City"].unique())

# df["FavSub"] = df["FavSub"].fillna("Unknown")
# df["City"] = df["City"].fillna("Unknown")
# df["Ad"] = df["Ad"].fillna(120 - df["Pd"])
# print(df)


# for i in range(len(df)):
#     if df.iloc[i].isnull().sum() > 0:
#         print(df["Name"][i])


# df = df.dropna()
# print(df)
# print(df.isnull().sum())
# print(df.duplicated())

# df["ComingMethod"]=df["ComingMethod"].replace("Bus","SchoolBus")
# print(df)

# df = df.drop_duplicates()
# print(df)

df.rename(columns={"Result":"Marks"}, inplace=True)
print(df)
