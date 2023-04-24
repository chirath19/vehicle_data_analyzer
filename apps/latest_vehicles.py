import pandas as pd
from dash import html

df_new = pd.read_csv('final_details.csv')
df_newly_added = pd.read_csv('final_new_details.csv')
df_newly_added['Brand Name'] = df_newly_added['Brand Name'].astype(str)
df_new['Posted Date'] = pd.to_datetime(df_new['Posted Date'])
dropdown_options = [{'label': x, 'value': x} for x in df_new['Brand Name'].unique()]
brand_names = [{'label': str(brand), 'value': brand} for brand in
               sorted(df_new['Brand Name'].unique())]

# Define a function to clean and convert the values to numbers
import re


def clean_and_convert(value):
    value = str(value).replace('$', '').replace(',', '').replace('/yr', '').replace('\n', '').strip()
    value = re.sub(r'[^\d.]+', '', value)
    if value == '..':
        return 0
    else:
        return float(value)


# Use apply function to apply the clean_and_convert function to all elements of the 'price' column
df_new['depreciation'] = df_new['depreciation'].apply(clean_and_convert)
df_new['price'] = df_new['price'].apply(clean_and_convert)

layout = html.Div([
])
