# Importing libraries
import pandas as pd
import numpy as np
from dash import Dash, html, dcc
import plotly.express as px



# Data loading
data = pd.read_csv(r'https://raw.githubusercontent.com/automat9/Projects/refs/heads/master/University%20Projects/Programming%20for%20Business%20Analytics/coffee%20company/raw%20coffee%20dataset.csv')

### Data preparation
# remove white space
data.columns = data.columns.str.strip()

# remove unnecessary columns as there is already a date column, inplace permanently changes the original dataset
data.drop(columns=['Month Number','Month Name','Year'], inplace = True)

# rename Sales to Net Sales for clarity
data.rename(columns={'Sales':'Net Sales ($)'}, inplace = True)

# rename column names to include ($)
data.columns = [f'{column} ($)' 
                if column in ['Units Sold', 'Manufacturing Price', 'Sale Price', 
                              'Gross Sales', 'Discounts', 'COGS','Profit'] 
                else column for column in data.columns]

# move date and product to the front
data = data[['Date', 'Product'] + [column for column in data.columns if column != 'Date' and column != 'Product']]

# sort by date, ascending order
data = data.sort_values(by='Date', ascending = True)

# reset index (to reflect the new order)
data = data.reset_index(drop = True)

# further data cleaning
for column in ['Profit ($)', 'Net Sales ($)', 'Gross Sales ($)', 'Discounts ($)', 'Sale Price ($)', 'COGS ($)', 'Manufacturing Price ($)']:
    if column in data.columns:
        data[column] = (data[column]
                        .astype(str) # convert to string to use .str methods
                        .str.strip()
                        .replace({'\\$': ''}, regex = True)
                        .str.replace(',','')
                        .str.replace('-','')
                        .replace(r'\((.*?)\)', r'-\1', regex=True) # AI generated (represents negatives with - instead of ())
                        .replace(['', 'N/A'], '0') # replace empty strings and N/A with NaN
                        .astype(float))
    
### Data Analysis
pd.options.display.float_format = '{:,.2f}'.format # two decimal places instead of x.xxxe+03

print(data.describe()) # eyeball analysis

questionable_units = data[data['Profit ($)'] <= 0].shape[0]
print(f'Total number of units with no profit or a loss {questionable_units}')



"""
Findings:
Total number of units with no profit or a loss 144

"""

### Data Visualisation
# data processing



data.head()
