# Import Libraries
import pandas as pd
import numpy as np
from dash import Dash, html, dcc
import plotly.express as px

# Settings
pd.options.display.float_format = '{:,.2f}'.format # adds thousands separator and rounds numbers to two decimal places instead of x.xxxe+03
pd.set_option('display.expand_frame_repr', False)

# Data Loading
data = pd.read_csv(r'https://raw.githubusercontent.com/automat9/Projects/refs/heads/master/University%20Projects/Programming%20for%20Business%20Analytics/coffee%20company/raw%20coffee%20dataset.csv')

### Data Preparation
# Remove Extra Space from Column Names
data.columns = data.columns.str.strip()

# Remove Extra Space from Columns Containing String Values 
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x) # AI generated

# Remove Unnecessary Columns as There is Already a Date Column, Inplace Permanently Changes the Original Dataset
data.drop(columns=['Month Number','Month Name','Year'], inplace = True)

# Rename Sales to Net Sales for Clarity
data.rename(columns={'Sales':'Net Sales ($)'}, inplace = True)

# Rename Column names to Include ($)
data.columns = [f'{column} ($)' 
                if column in ['Manufacturing Price', 'Sale Price', 
                              'Gross Sales', 'Discounts', 'COGS','Profit'] 
                else column for column in data.columns]

# Move Date and Product to the Front
data = data[['Date', 'Product'] + [column for column in data.columns if column != 'Date' and column != 'Product']]

# Sort by Date, Ascending Order
data = data.sort_values(by='Date', ascending = True)

# Reset Index (to reflect the new order)
data = data.reset_index(drop = True)

# Further Data Cleaning
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
# Initial Eyeball Analysis
#print(data.describe())

# How many Products Generate no Profit or a Loss
questionable_products = data[data['Profit ($)'] <= 0].shape[0]
#print(f'Total number of products with no profit or a loss: {questionable_products}')

# Most Profitable Products
most_profitable_products = data.nlargest(5, 'Profit ($)') # adjust to see more/fewer products
#print(most_profitable_products)

# Loss Generating Products
loss_generating_products = data.nsmallest(5, 'Profit ($)')
#print(loss_generating_products)

# Profit Margin per Segment
segments = data.groupby('Segment')['Profit ($)'].sum().sort_values(ascending = False)
#print(segments)

# Profit Margin per Country
countries = data.groupby('Country')['Profit ($)'].sum().sort_values(ascending = False)
#print(countries)

# Segments and Countries sorted by Profit
segments_countries = data.groupby(['Segment', 'Country'])['Profit ($)'].sum().sort_values(ascending = False)
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

# Customer Segmentation
segment_analysis = data.groupby('Segment').agg({
    'Units Sold': 'sum',
    'Gross Sales ($)': 'sum',
    'Net Sales ($)': 'sum',
    'Profit ($)': 'sum'})

segment_analysis['Profit Margin (%)'] = (segment_analysis['Profit ($)'] / segment_analysis['Net Sales ($)']) * 100
segment_analysis = segment_analysis.sort_values(by = 'Profit Margin (%)', ascending = False)
#print(segment_analysis)

#TODO
"""
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
Missing Costs (e.g. for index 0, COGS appears as $21,040.50, but COGS = Units Sold x Manufacturing Price = $9,468.23?)

Total number of units with no profit or a loss 144

Beverages is the most profitable segment, Packaged and Prepared Food only generates a loss

There are many more products that generate a loss than those that generate exceptionally high sales

The 'Low' discount band has the highest average profit per unit

COGS of 21.52% of products are 90% or above, indicating low profitability

The profit margin of the Packaged and Prepared Foods Segment is -2.08%

"""

### Data Visualisation
# data processing


#data.query("`Profit ($)` > 50000 and Country == 'China' and `COGS Ratio (%)` > 0.9")
#data.head()
