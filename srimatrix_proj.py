# Step 1. Import the necessary libraries
import pandas as pd
import datetime

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple_data = pd.read_csv(url)
# print (apple_data)
# Checkout the type of columns

print (apple_data)
# print(apple_data.dtypes)
# dups = apple_data['Date']
# print('Hell')
# # df[ids.isin(ids[ids.duplicated()])].sort("ID")
# apple_data[dups.isin(dups[dups.duplicated()])].sort_values("Date")
print(apple_data)
# Step 5. Transform the Date column as a datetime type
# print('***',apple_data.dtypes.get_value['Date'])
print('hello')
apple_data['Date'] = pd.to_datetime(apple_data['Date'].str.strip(), format = '%Y-%m-%d')
print(apple_data['Date'])
# Step 6. Set the date as the index
# apple_data.set_index('Date', inplace=True)

# print('^^^', apple_data)
boolean = not apple_data["Date"].is_unique 


# Step 7. Is there any duplicate dates?
# dups = apple_data[['Date']]
# print('Hell')
# # df[ids.isin(ids[ids.duplicated()])].sort("ID")
# apple_data[dups.isin(dups[dups.duplicated()])].sort("Date")

