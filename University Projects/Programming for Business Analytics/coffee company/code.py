# Importing libraries
import pandas as pd
import numpy as np
from dash import Dash, html, dcc
import plotly.express as px

# Data loading
data = pd.read_csv(r'https://raw.githubusercontent.com/automat9/Projects/refs/heads/master/University%20Projects/Programming%20for%20Business%20Analytics/coffee%20company/dataset.csv')

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

# remove $ from cells for easier data manipulation
for column in data.columns:
    data[column] = data[column].replace({'\\$': ''}, regex = True)

# move date and product to the front
data = data[['Date', 'Product'] + [column for column in data.columns if column != 'Date' and column != 'Product']]

# sort by date, ascending order
data = data.sort_values(by='Date', ascending = True)

# reset index (to reflect the new order)
data = data.reset_index(drop = True)

# further data cleaning
for column in ['Profit ($)', 'Sales ($)', 'Gross Sales ($)', 'Discounts ($)', 'COGS ($)']:
    if column in data.columns:
        data[column] = (data[column]
                        .astype(str) # convert to string to use .str methods
                        .str.strip()
                        .str.replace('[()]', '', regex = True)
                        .str.replace(',','')
                        .str.replace('-','')
                        .replace(['', 'N/A'], np.nan) # replace empty strings and N/A with NaN
                        .astype(float))
    
# TODO: TRY TO MOVE $ REMOVAL TO FURTHER DATA CLEANING



### Data Analysis
# mean etc

### Data Visualisation
# data processing



data.head()
