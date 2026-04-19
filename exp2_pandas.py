import pandas as pd

data = {
    "Name": ["Alya", "Riya", "Karan", "Aman"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("\nHead:\n", df.head())

print("\nInfo:")
print(df.info())

print("\nDescribe:\n", df.describe())

print("\nSelect Column:\n", df["Name"])

print("\nFilter (Marks > 80):\n", df[df["Marks"] > 80])

df["Grade"] = ["A", "A+", "B", "A"]
print("\nAfter Adding Column:\n", df)