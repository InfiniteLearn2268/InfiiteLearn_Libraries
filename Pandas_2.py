import pandas as pd

# ======================================================
#               PANDAS PART 2 (BEGINNER GUIDE)
# ======================================================

# -------------------------------
# 1. Reading CSV File
# -------------------------------

# data = pd.read_csv('Titanic-Dataset.csv')
# df = pd.DataFrame(data)
# print(df)


# -------------------------------
# 2. Access Single Value
# -------------------------------

# at  → label-based access (fast)
# iat → position-based access (fast)

# Example (column must exist)
# print(df.at[1, 'Fare'])     # Row label + column name
# print(df.iat[2, 3])         # Row index + column index


# -------------------------------
# 3. Delete Row
# -------------------------------

# Delete row with index 0
# df.drop(0, inplace=True)


# -------------------------------
# 4. Create DataFrame Manually
# -------------------------------

data = {
    "Name": ["A", "B", "C", "D"],
    "City": ["Jalgaon", "Mumbai", "Delhi", "Kolkata"],
    "Marks": [23.0, 22.0, 60.5, None]   # None = missing value
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


# -------------------------------
# 5. Handling Missing Values
# -------------------------------

# Check missing values (True/False)
print("\nMissing Values:\n", df.isnull())

# Check if any missing in each column
print("\nAny missing in columns:\n", df.isnull().any(axis=0))

# Count missing values per column
print("\nMissing count:\n", df.isnull().sum())


# -------------------------------
# 6. Fill Missing Values
# -------------------------------

# Fill all missing values with 0
print("\nFill with 0:\n", df.fillna(0))

# Fill missing Marks with mean
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print("\nAfter filling with mean:\n", df)


# -------------------------------
# 7. Rename Columns
# -------------------------------

df = df.rename(columns={'Name': 'New_Name'})
print("\nAfter renaming column:\n", df)


# -------------------------------
# 8. Modify Column Values
# -------------------------------

# Example: increase Marks by 10
df['Marks'] = df['Marks'] + 10
print("\nAfter modifying Marks:\n", df)


# -------------------------------
# 9. Apply Function (Lambda)
# -------------------------------

# Square of Marks
df['Marks_Squared'] = df['Marks'].apply(lambda x: x**2)
print("\nAfter applying lambda:\n", df)


# -------------------------------
# 10. Change Data Type
# -------------------------------

# Convert Marks to integer
df['Marks_Int'] = df['Marks'].astype(int)
print("\nAfter type conversion:\n", df)


# ======================================================
#           DATA AGGREGATION & GROUPING
# ======================================================

# Load dataset (ensure file exists)
data_csv = pd.read_csv('Titanic-Dataset.csv', skipinitialspace=True)

# -------------------------------
# 11. GroupBy (Single Column)
# -------------------------------

# NOTE: Column names must match your dataset exactly

# group_mean = data_csv.groupby('City')['Marks'].mean()
# print("\nGroupBy Mean:\n", group_mean)


# 12 . NEXT CONCEPT IS GROUPBY ON MUTIPLE COLUMNS 