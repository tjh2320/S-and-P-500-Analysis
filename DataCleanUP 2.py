import pandas as pd

# 1. sp500_companies.csv data cleaning

# Load the dataset
data = pd.read_csv('S&P Data From Kagal/sp500_companies.csv')

# Check for missing values
print(data.isnull().sum())

# Fill missing values or drop rows
data['Ebitda'].fillna(0, inplace=True)
data['Revenuegrowth'].fillna(0, inplace=True)
data['State'].fillna('Unknown', inplace=True)
data['Fulltimeemployees'].fillna(0, inplace=True)

# Check data types
print(data.dtypes)

# Convert columns to appropriate data types if necessary
# In this case, all columns seem to have appropriate types, so this step might not be needed

# Remove duplicates
data.drop_duplicates(inplace=True)

# Detect and handle outliers (example for Currentprice)
# You can define lower_bound and upper_bound based on your data
lower_bound = data['Currentprice'].quantile(0.01)
upper_bound = data['Currentprice'].quantile(0.99)
data = data[(data['Currentprice'] >= lower_bound) & (data['Currentprice'] <= upper_bound)]

# Save the cleaned data
data.to_csv('cleaned_data_companies.csv', index=False)


#2. sp500_stocks.csv data cleaning


# Load the dataset
data = pd.read_csv('S&P Data From Kagal/sp500_index.csv')

# Check for missing values
print(data.isnull().sum())

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Check data types
print(data.dtypes)

# Assuming no duplicates are expected for 'Date', but if needed:
data.drop_duplicates(inplace=True)

# Detect and handle outliers for 'S&P500' (example)
# Define lower and upper bounds based on your criteria
lower_bound = data['S&P500'].quantile(0.01)
upper_bound = data['S&P500'].quantile(0.99)
data = data[(data['S&P500'] >= lower_bound) & (data['S&P500'] <= upper_bound)]

# Save the cleaned data
# data.to_csv('cleaned_data_index.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_data.csv'.")


# 3. sp500_stocks.csv data cleaning

# Load the dataset
data = pd.read_csv('S&P Data From Kagal/sp500_stocks.csv')

# Check for missing values
print(data.isnull().sum())

# Fill missing values for numerical columns with 0
data['Adj Close'].fillna(0, inplace=True)
data['Close'].fillna(0, inplace=True)
data['High'].fillna(0, inplace=True)
data['Low'].fillna(0, inplace=True)
data['Open'].fillna(0, inplace=True)
data['Volume'].fillna(0, inplace=True)

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Check data types
print(data.dtypes)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Detect and handle outliers in the 'Close' column
lower_bound = data['Close'].quantile(0.01)
upper_bound = data['Close'].quantile(0.99)
data = data[(data['Close'] >= lower_bound) & (data['Close'] <= upper_bound)]

# Save the cleaned data
data.to_csv('cleaned_data_stocks.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_data.csv'.")
