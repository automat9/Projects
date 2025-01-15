# Importing libraries
import pandas as pd
import matplotlib as plt

# Data loading
data = pd.read_csv(r'https://raw.githubusercontent.com/automat9/Projects/refs/heads/master/University%20Projects/Programming%20for%20Business%20Analytics/coffee%20company/dataset.csv')

### Data preparation
# remove white space
data.columns = data.columns.str.strip()

# remove unnecessary columns as there is already a date column, inplace permanently changes the original dataset
data.drop(columns=['Month Number','Month Name','Year'], inplace = True)

# rename Sales to Net Sales for clarity
data.rename(columns={'Sales':'Net Sales ($)'}, inplace = True)

# replace "-" with "N/A" in the discount column for clarity
data['Discounts'] = data['Discounts'].astype(str).str.replace('-', 'N/A')

# rename column names to include $, remove $ from cells for easier data manipulation
data.columns = [f'{column} ($)' 
                if column in ['Units Sold', 'Manufacturing Price', 'Sale Price', 
                              'Gross Sales', 'Discounts', 'COGS','Profit'] 
                else column for column in data.columns]

for column in data.columns:
    data[column] = data[column].replace({'\$': ''}, regex = True)


data.head()
