import pandas as pd

# PANDAS PART 1 
#  1. SERIES


# A) List to Series
# Converts list → pandas Series (1D array)

data = [1, 2, 3, 4, 5]
series_1 = pd.Series(data)
print("Series from List:\n", series_1)


# B) Dictionary to Series
# Keys become index, values become data

data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series_2 = pd.Series(data_dict)
print("\nSeries from Dictionary:\n", series_2)


# C) Custom Indexing
# You can define your own index labels

data = [10, 20, 30, 40]
index = ['g', 'h', 'i', 'j']
series_3 = pd.Series(data, index=index)
print("\nSeries with Custom Index:\n", series_3)



#  2. DATAFRAME CREATION


# A) From Dictionary of Lists
# Each key = column name

data = {
    'Name': ['Deva', 'Bhushan', 'Javed'],
    'RollNo': [12, 13, 14],
    'College': ['DYP', 'VIT', 'COEP']
}

df1 = pd.DataFrame(data)
print("\nDataFrame from Dictionary:\n", df1)


# B) From List of Dictionaries
# Each dictionary = row

data = [
    {'Name': 'Deva', 'Age': 32, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 23, 'City': 'Canada'},
    {'Name': 'Salman', 'Age': 58, 'City': 'Bandra'}
]

df2 = pd.DataFrame(data)
print("\nDataFrame from List of Dictionaries:\n", df2)



#  3. READING CSV FILE


# Reads CSV file into DataFrame

df = pd.read_csv('Titanic-Dataset.csv')

# View first and last rows
print("\nTop 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())


# Access specific columns
print("\nPassengerId Column:\n", df['PassengerId'])



#  4. LOC vs ILOC


# loc → label based
# iloc → position based

print("\nUsing loc (label):\n", df.loc[0])
print("\nUsing iloc (position):\n", df.iloc[0])



#  6. DATA MANIPULATION


# 1) Add new column
df["Salary"] = 10000   # Adds same value to all rows
print("\nAfter Adding Salary:\n", df.head())


# 2) Delete column


# Note: axis = 0 (for rows ) 
# Note: axis = 1 (for columns ) 

# Method 1
# df.drop('Salary', axis=1, inplace=True)

# Method 2 (recommended)
# df.drop(columns=['Salary'], inplace=True)






#  7. INFORMATION FUNCTIONS


# Check data types
print("\nData Types:\n", df.dtypes)

# Statistical summary
print("\nStatistical Summary:\n", df.describe())



