# Import Libraries
import pandas as pd
import numpy as np
from dash import Dash, html, dcc
import plotly.express as px

# Settings
pd.options.display.float_format = '{:,.2f}'.format # adds thousands separator and rounds numbers to two decimal places instead of x.xxxe+03
pd.set_option('display.expand_frame_repr', False) # output display settings

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

# Create a COGS Ratio Column
data['COGS Ratio (%)'] = (data['COGS ($)'] / data['Net Sales ($)']) * 100

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
#print(data[['Units Sold', 'Manufacturing Price ($)','COGS ($)', 'Net Sales ($)', 'COGS Ratio (%)']].head())

threshold = 0.9
high_cogs_ratio = data.loc[data['COGS Ratio (%)'] > threshold, 'COGS Ratio (%)'].count()
#print(f"Total number of high COGS ratio products: {high_cogs_ratio} / {data['COGS Ratio (%)'].count()}")
#print(f"Proportion of products that have high COGS ratio: {high_cogs_ratio / data['COGS Ratio (%)'].count()}")

# Profit Margin per Segment
segments = data.groupby('Segment')['Profit ($)'].sum().sort_values(ascending = False)
#print(segments)

# Full Segment Analysis
segment_analysis = data.groupby('Segment').agg({
    'Units Sold': 'sum',
    'Gross Sales ($)': 'sum',
    'Net Sales ($)': 'sum',
    'Profit ($)': 'sum'})

segment_analysis['Profit Margin (%)'] = (segment_analysis['Profit ($)'] / segment_analysis['Net Sales ($)']) * 100
segment_analysis = segment_analysis.sort_values(by = 'Profit Margin (%)', ascending = False)
#print(segment_analysis)

# Profit Margin per Country
countries = data.groupby('Country')['Profit ($)'].sum().sort_values(ascending = False)
#print(countries)

# Full Country-wise Performance
country_performance = data.groupby("Country").agg({
    'Units Sold': 'sum',
    'Gross Sales ($)': 'sum',
    'Net Sales ($)': 'sum',
    'Profit ($)': 'sum'})

country_performance['Profit Margin (%)'] = (country_performance['Profit ($)'] / country_performance['Net Sales ($)']) * 100
country_performance = country_performance.sort_values(by = "Profit Margin (%)", ascending=False)
#print(country_performance)

# Full Segments and Countries Analysis
segments_countries = data.groupby(['Segment', 'Country']).agg({
    'Profit ($)': 'sum',
    'Net Sales ($)': 'sum'})

segments_countries['Profit Margin (%)'] = (segments_countries['Profit ($)'] / segments_countries['Net Sales ($)']) * 100

segments_countries = segments_countries.sort_values(by='Profit Margin (%)', ascending=False)
#print(segments_countries)

# Correlation Analysis
correlation = ['Discounts ($)', 'Gross Sales ($)', 'Profit ($)']
#print(data[correlation].corr())

# Outlier Detection in Profit and Discounts
profit_q1 = data['Profit ($)'].quantile(0.25)
profit_q3 = data['Profit ($)'].quantile(0.75)
discount_q1 = data['Discounts ($)'].quantile(0.25)
discount_q3 = data['Discounts ($)'].quantile(0.75)

profit_iqr = profit_q3 - profit_q1
discount_iqr = discount_q3 - discount_q1

lower_bound_profit = profit_q1 - 1.5 * profit_iqr
upper_bound_profit = profit_q3 + 1.5 * profit_iqr
lower_bound_discount = discount_q1 - 1.5 * discount_iqr
upper_bound_discount = discount_q3 + 1.5 * discount_iqr 

profit_outliers = data[(data['Profit ($)'] < lower_bound_profit) | (data['Profit ($)'] > upper_bound_profit)]
discount_outliers = data[(data['Discounts ($)'] < lower_bound_discount) | (data['Discounts ($)'] > upper_bound_discount)]

#print("Number of outliers in Profit:", profit_outliers.shape[0])
#print(profit_outliers[['Profit ($)']])
#print("Number of outliers in Discounts:", discount_outliers.shape[0])
#print(discount_outliers[['Discounts ($)']])


#TODO
# Visualisation 


"""
Findings:
Missing Costs (e.g. for index 0, COGS appears as $21,040.50, but COGS = Units Sold x Manufacturing Price = $9,468.23?)

Total number of units with no profit or a loss 144

Beverages is the most profitable segment, Packaged and Prepared Food only generates a loss

There are many more products that generate a loss than those that generate exceptionally high sales

The 'Low' discount band has the highest average profit per unit

COGS of 21.52% of products are 90% or above, indicating low profitability

The worst profit margin is that of the Packaged and Prepared Foods segment: -2.08%
The best profit margin is that of the DIary Products segment: 56.32%

The worst profit margin is that of China: 9.44%
The best profit margin is that of Japan 11.88%
"""

### Data Visualisation
# data processing


#data.query("`Profit ($)` > 50000 and Country == 'China' and `COGS Ratio (%)` > 0.9")
#data.head()
