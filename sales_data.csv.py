import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style='whitegrid')
df=pd.read_csv('sales_data.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())

if 'sales' not in df.columns:
    df['sales']=df['quantity']*df['price']
df['date']=pd.to_datetime(df['date'])
monthly_sales=df.resample('m',on='date')['sales'].sum()
plt.figure(figsize=(12,6))
monthly_sales.plot(marker='o')
plt.title('monthly sales trend')
plt.xlabel('month')
plt.ylabel('sales')
plt.grid(True)
plt.show()

top_products=df.groupby('product')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values,y=top_products.index,palette='viridis')
plt.title('top 10 products by sales')
plt.xlabel('sales')
plt.ylabel('products')
plt.show()

region_sales=df.groupby('region')['sales'].sum().sort_values(ascending=False)


plt.figure(figsize=(8,5))
region_sales.plot(kind='pie',autopct='%1.1f%%',startangle=140)
plt.title('sales distribution by region')
plt.ylabel('')
plt.show()

category_sales=df.groupby('category')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=category_sales.index,y=category_sales.values, palette='pastel')
plt.title('sales by category')
plt.xlabel('category')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
plt.title('correlation heatmap')
plt.show()
