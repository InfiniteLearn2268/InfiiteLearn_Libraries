
# SEABORN + MATPLOTLIB VISUALIZATION FILE


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = sns.load_dataset('tips')


# BASIC INFO

print(df.head())
print(df.info())


# 1. SCATTER PLOT

sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('Scatter Plot: Total Bill vs Tip')
plt.show()



# 2. LINE PLOT

sns.lineplot(x='size', y='total_bill', data=df)
plt.title('Line Plot')
plt.show()



# 3. BAR PLOT (CATEGORICAL)

sns.barplot(x='day', y='total_bill', data=df, palette='deep')
plt.title('Average Total Bill per Day')
plt.show()






# 4. HISTOGRAM

sns.histplot(df['total_bill'], bins=10, kde=True)
plt.title('Histogram with KDE')
plt.show()



# 5. KDE (DENSITY PLOT)

sns.kdeplot(df['total_bill'], fill=True)
plt.title('KDE Plot')
plt.show()






# 6. HEATMAP (CORRELATION)

corr = df[['total_bill', 'tip', 'size']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
print("Correlation Matrix:\n", corr)
plt.show()



# 7. WORKING WITH EXCEL DATA


# Uncomment when you have file
# sales = pd.read_excel('sales_data.xlsx')

# Preview data
# print(sales.head())

# --- BAR PLOT: Product vs Sales ---
# sns.barplot(x='Product', y='Sales', data=sales)
# plt.title('Sales by Product')
# plt.show()

# --- BAR PLOT: Region vs Sales ---
# sns.barplot(x='Region', y='Sales', data=sales)
# plt.title('Sales by Region')
# plt.show()



# END OF FILE
