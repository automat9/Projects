import pandas as pd

# Load data from GitHub URL and reorder columns
url = "https://github.com/automat9/Business-Analytics/raw/aadac54eaf6f4ca76c4970a1d317ad355a7fe051/Semester%201/Programming%20for%20Business%20Analytics/Midterm%20Project/Coffee_company.csv"
data = pd.read_csv(url)

new_order = [
    'Date', 'Year', 'Month Number', ' Month Name ', 'Segment', 'Country', ' Product ', 
    ' Discount Band ', 'Units Sold', ' Manufacturing Price ', ' Sale Price ', 
    ' Gross Sales ', ' Discounts ', '  Sales ', ' COGS ', ' Profit '
]
sorted_data = data[new_order]

# Clean and convert 'Sales' and 'Profit' columns
data['Sales'] = pd.to_numeric(data['  Sales '].replace('[\$,]', '', regex=True), errors='coerce')
data['Profit'] = pd.to_numeric(data[' Profit '].replace('[\$,]', '', regex=True), errors='coerce')

# Calculate total sales and profit by product
product_performance = data.groupby(data[' Product '].str.strip()).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Display each product's sales and profit
# Note to self: "_, row" is commonly used in loops to indicate that we are only interested in the row content, not the index
for _, row in product_performance.iterrows():
    print(f"Product: {row[' Product ']}, Sales: £{row['Sales']}, Profit: £{row['Profit']}")

# Display highest and lowest sales and profit products
for metric in ['Sales', 'Profit']:
    highest = product_performance.loc[product_performance[metric].idxmax()]
    lowest = product_performance.loc[product_performance[metric].idxmin()]
    print(f"Highest {metric} Product: {highest[' Product ']}, {metric}: £{highest[metric]}")
    print(f"Worst {metric} Product: {lowest[' Product ']}, {metric}: £{lowest[metric]}")
