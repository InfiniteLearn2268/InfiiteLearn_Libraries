import pandas as pd
from io import StringIO

# ======================================================
#     DATA AGGREGATION & GROUPING (GROUPBY)
# ======================================================

# Sample DataFrame
data = {
    "Name": ["A", "A", "B", "B", "C"],
    "City": ["Jalgaon", "Mumbai", "Jalgaon", "Mumbai", "Jalgaon"],
    "Marks": [90, 80, 70, 60, 50]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


# -------------------------------
# 1. GroupBy (Multiple Columns)
# -------------------------------

# Group by Name and City → sum of Marks
gb = df.groupby(['Name', 'City'])['Marks'].sum()
print("\nGroupBy (Name + City):\n", gb)


# -------------------------------
# 2. Multiple Aggregate Functions
# -------------------------------

# Apply mean, sum, count on Marks grouped by City
agg_result = df.groupby('City')['Marks'].agg(['mean', 'sum', 'count'])
print("\nMultiple Aggregations:\n", agg_result)


# ======================================================
#           MERGING / JOINING DATAFRAMES
# ======================================================

df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C'],
    'Value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'Key': ['A', 'B', 'D'],
    'Value2': [4, 5, 6]
})

# Inner Join → only matching keys
print("\nInner Merge:\n", pd.merge(df1, df2, how='inner'))

# Outer Join → all keys
print("\nOuter Merge:\n", pd.merge(df1, df2, how='outer'))

# Left Join → all keys from df1
print("\nLeft Merge:\n", pd.merge(df1, df2, how='left'))

# Right Join → all keys from df2
print("\nRight Merge:\n", pd.merge(df1, df2, how='right'))


# ======================================================
#           READING DATA FROM URL
# ======================================================

# Read CSV from URL
# url_data = pd.read_csv(
#     "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
#     header=None
# )
# print("\nData from URL:\n", url_data)

# Save DataFrame to CSV file
# url_data.to_csv('myfile.csv', index=False)


# ======================================================
#           READ TABLE FROM WEBSITE
# ======================================================

# url = "https://www.fdic.gov/bank-failures/failed-bank-list"

# Read tables from webpage
# tables = pd.read_html(url)

# Print first table
# print("\nHTML Table:\n", tables[0])


# ======================================================
#           READING EXCEL FILE
# ======================================================

# df_excel = pd.read_excel('product.xlsx')
# print("\nExcel Data:\n", df_excel)


# ======================================================
#           JSON HANDLING
# ======================================================

# JSON String
json_data = '''
[
 {"Name":"A","City":"Jalgaon","Marks":90},
 {"Name":"B","City":"Mumbai","Marks":80},
 {"Name":"C","City":"Jalgaon","Marks":30}
]
'''

# Convert JSON string → DataFrame
df_json = pd.read_json(StringIO(json_data))
print("\nJSON to DataFrame:\n", df_json)

# Convert DataFrame → JSON
print("\nBack to JSON:\n", df_json.to_json())

# Different JSON formats (orient)

print("\nJSON (index format):\n", df_json.to_json(orient='index'))
print("\nJSON (records format):\n", df_json.to_json(orient='records'))


#  NEXT CONCEPT IS MATPLOTLIB 