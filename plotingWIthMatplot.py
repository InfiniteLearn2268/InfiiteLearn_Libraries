# 📊 Matplotlib Complete Guide (Beginner to Intermediate)

import matplotlib.pyplot as plt
import pandas as pd



#  1. LINE PLOT



"""
Basic Line Plot Example
"""

x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 16, 25]

plt.figure(figsize=(6,4))
plt.plot(x, y, color='red', linestyle='--', marker='o', linewidth=2, markersize=8)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot Example")
plt.grid(True)

plt.show()



#  2. MULTIPLE SUBPLOTS



"""
Displaying multiple plots in one figure
"""

z = [1, 3, 5, 7, 8]
m = [10, 20, 30, 40, 50]

plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.plot(x, y, color='green')
plt.title("Plot 1")

plt.subplot(2,2,2)
plt.plot(x, z, color='red')
plt.title("Plot 2")

plt.subplot(2,2,3)
plt.plot(y, z, color='blue')
plt.title("Plot 3")

plt.subplot(2,2,4)
plt.plot(x, m, color='purple')
plt.title("Plot 4")

plt.tight_layout()
plt.show()



#  3. BAR PLOT



"""
Bar chart for categorical data
"""

category = ['A','B','C','D','E']
value = [5,10,25,35,45]

plt.figure(figsize=(6,4))
plt.bar(category, value, color='purple')

plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Bar Chart Example")

plt.show()



#  4. HISTOGRAM



"""
Distribution of data
"""

data = [1,2,3,1,3,4,5,1,3,2,1,3,5,1]

plt.figure(figsize=(6,4))
plt.hist(data, bins=5, color='red', edgecolor='black')

plt.title("Histogram Example")
plt.show()



#  5. SCATTER PLOT



"""
Relationship between two variables
"""

plt.figure(figsize=(6,4))
plt.scatter(x, y, color='red', marker='X')

plt.title("Scatter Plot Example")
plt.show()



#  6. PIE CHART



"""
Proportion visualization
"""

labels = ['A','B','C']
sizes = [30,20,40]
colors = ['gold','green','lightskyblue']
explode = (0.1, 0, 0)

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct="%1.2f%%", shadow=True)

plt.title("Pie Chart Example")
plt.show()



#  7. REAL-WORLD EXAMPLE (SALES DATA)



"""
Working with dataset
"""

df = pd.read_excel('sales_data.xlsx')
print(df.head())



#  7.1 Sales by Product (Bar Chart)



sales_by_product = df.groupby('Product')['Sales'].sum()

plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='red')

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()



#  7.2 Sales Trend Over Time (Line Plot)



sales_trend = df.groupby('Date')['Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(sales_trend['Date'], sales_trend['Sales'], color='blue', marker='o')

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.grid(True)

plt.show()


