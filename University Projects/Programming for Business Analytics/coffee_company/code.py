import pandas as pd

# Load data from new GitHub URL and reorder columns
data = pd.read_csv(r'https://github.com/automat9/Projects/raw/50440f4e43b70aba6f5743102f7d73455112f43f/University%20Projects/Programming%20for%20Business%20Analytics/coffee_company_dataset.csv')

new_order = [
    'Date', 'Year', 'Month Number', ' Month Name ', 'Segment', 'Country', ' Product ', 
    ' Discount Band ', 'Units Sold', ' Manufacturing Price ', ' Sale Price ', 
    ' Gross Sales ', ' Discounts ', '  Sales ', ' COGS ', ' Profit ']

sorted_data = data[new_order]

# Clean and convert 'Sales' and 'Profit' columns
data['Sales'] = pd.to_numeric(data['  Sales '].replace('[\$,]', '', regex=True), errors='coerce')
data['Profit'] = pd.to_numeric(data[' Profit '].replace('[\$,]', '', regex=True), errors='coerce')

# Calculate total sales and profit by product
product_performance = data.groupby(data[' Product '].str.strip()).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Display each product's sales and profit
for _, row in product_performance.iterrows():
    print(f"Product: {row[' Product ']}, Sales: £{row['Sales']}, Profit: £{row['Profit']}")

# Display highest and lowest sales and profit products
for metric in ['Sales', 'Profit']:
    highest = product_performance.loc[product_performance[metric].idxmax()]
    lowest = product_performance.loc[product_performance[metric].idxmin()]
    print(f"Highest {metric} Product: {highest[' Product ']}, {metric}: £{highest[metric]}")
    print(f"Worst {metric} Product: {lowest[' Product ']}, {metric}: £{lowest[metric]}")
