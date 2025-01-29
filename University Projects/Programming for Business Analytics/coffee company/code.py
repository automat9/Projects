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
                if column in ['Manufacturing Price', 'Sale Price', 
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

# initial eyeball analysis
#print(data.describe())

# How many products generate no profit or a loss
questionable_products = data[data['Profit ($)'] <= 0].shape[0]
#print(f'Total number of products with no profit or a loss: {questionable_products}')

# Most profitable Products
most_profitable_products = data.nlargest(20, 'Profit ($)') # adjust to see more/fewer products
#print(best_performing_products)

# Loss Generating Products
loss_generating_products = data.nsmallest(20, 'Profit ($)')
#print(loss_generating_products)

# Profit Margin per Segment
segments = data.groupby('Segment')['Profit ($)'].sum().sort_values(ascending = False)
#print(segments)

# Profit Margin per Country
countries = data.groupby('Country')['Profit ($)'].sum().sort_values(ascending = False)
#print(countries)

# Segments and Countries sorted by Profit
segments_countries = data.groupby(['Segment', 'Country'])['Profit ($)'].sum().sort_values(ascending=False)
#print(segments_countries)

# Discount Band Impact on Sales and Profit
discount_impact = data.groupby('Discount Band').agg(
    total_units_sold = ('Units Sold', 'sum'),
    total_profit= ('Profit ($)', 'sum'))

discount_impact['average_profit_per_unit'] = (discount_impact['total_profit'] / discount_impact['total_units_sold'])
#print(discount_impact)

# Cost Efficiency 
data['COGS Ratio (%)'] = (data['COGS ($)'] / data['Net Sales ($)'])
#print(data[['Units Sold', 'Manufacturing Price ($)','COGS ($)', 'Net Sales ($)', 'COGS Ratio (%)']].head())

threshold = 0.9
high_cogs_ratio = data.loc[data['COGS Ratio (%)'] > threshold, 'COGS Ratio (%)'].count()
#print(f"Total number of high COGS ratio products: {high_cogs_ratio} / {data['COGS Ratio (%)'].count()}")
#print(f"Proportion of products that have high COGS ratio: {high_cogs_ratio / data['COGS Ratio (%)'].count()}")


#TODO
"""
Customer Segmentation:
Analyze segment-based performance trends.

Country-wise Performance:
Explore geographical performance for revenue and profit.

Correlation Analysis:
Investigate relationships between Discounts ($), Gross Sales ($), and Profit ($).

Forecasting:
Use Date and sales data for time series forecasting of future sales.

Outlier Detection:
Identify anomalies in Profit ($) or Discounts ($).
"""

"""
Findings:
Not all data is included (e.g. for index 0, COGS appears as $21,040.50, but COGS = Units Sold x Manufacturing Price = $9,468.23?)

Total number of units with no profit or a loss 144

Beverages is the most profitable segment, Packaged and Prepared Food only generates a loss

There are many more products that generate a loss than those that generate exceptionally high sales

The 'Low' discount band has the highest average profit per unit

COGS of 21.52% of products are 90% or above, indicating low profitability


"""

### Data Visualisation
# data processing



data.head()
