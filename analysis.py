import pandas as pd

df = pd.read_csv('data/customer_data.csv', encoding='latin1')
# Remove nulls
df = df.dropna(subset=['CustomerID'])

# Revenue
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Group by customer
customer_df = df.groupby('CustomerID').agg({
    'Revenue': 'sum',
    'InvoiceNo': 'nunique'
}).reset_index()

customer_df.columns = ['CustomerID', 'TotalRevenue', 'TotalOrders']

# Segmentation
def segment(row):
    if row['TotalRevenue'] > 10000:
        return 'High Value'
    elif row['TotalRevenue'] > 5000:
        return 'Medium Value'
    else:
        return 'Low Value'

customer_df['Segment'] = customer_df.apply(segment, axis=1)

print(customer_df.head())