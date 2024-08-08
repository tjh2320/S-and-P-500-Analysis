import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the datasets
stocks_df = pd.read_csv('cleaned_data_stocks.csv')
companies_df = pd.read_csv('cleaned_data_companies.csv')
data_df = pd.read_csv('cleaned_data.csv')

# Filter data for the past 10 years
recent_data_df = stocks_df[stocks_df['Date'] >= '2013-01-01']

# Merge stocks_df with companies_df on the 'Symbol'
merged_df = pd.merge(recent_data_df, companies_df, on='Symbol')

# Calculate annual return using logarithmic returns to avoid infinite values
merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df['Year'] = merged_df['Date'].dt.year

# Calculate Log Return and Annual Return using transform to ensure index alignment
log_returns = merged_df.groupby(['Symbol', 'Year'])['Adj Close'].transform(lambda x: np.log(x / x.shift(1)))
log_returns = log_returns.fillna(0)  # Handle NaN values

merged_df['Log_Return'] = log_returns
merged_df['Annual_Return'] = merged_df.groupby(['Symbol', 'Year'])['Log_Return'].transform(lambda x: x.cumsum())

# Debug: Check if annual returns are calculated correctly
print(merged_df[['Symbol', 'Year', 'Adj Close', 'Annual_Return']].head(20))

# Rank stocks based on average annual return for each year
ranked_stocks = merged_df.groupby(['Year', 'Symbol'])['Annual_Return'].mean().reset_index()
ranked_stocks = ranked_stocks.replace([np.inf, -np.inf], np.nan).dropna()
ranked_stocks['Rank'] = ranked_stocks.groupby('Year')['Annual_Return'].rank(ascending=False)

# Identify top 10, middle 10, and bottom 10 stocks
top_10 = ranked_stocks.groupby('Year', group_keys=False).apply(lambda x: x.nlargest(10, 'Annual_Return')).reset_index(drop=True)
middle_10 = ranked_stocks.groupby('Year', group_keys=False).apply(lambda x: x.nlargest(20, 'Annual_Return').nsmallest(10, 'Annual_Return')).reset_index(drop=True)
bottom_10 = ranked_stocks.groupby('Year', group_keys=False).apply(lambda x: x.nsmallest(10, 'Annual_Return')).reset_index(drop=True)

# Debug: Check the top, middle, and bottom stocks
print("Top 10 Stocks")
print(top_10.head(20))
print("Middle 10 Stocks")
print(middle_10.head(20))
print("Bottom 10 Stocks")
print(bottom_10.head(20))

# Function to simulate investment
def simulate_investment(stocks, initial_investment=1000):
    investment_value = initial_investment
    investments = []
    
    for year in sorted(stocks['Year'].unique()):
        year_stocks = stocks[stocks['Year'] == year]
        annual_return = year_stocks['Annual_Return'].mean()
        investment_value *= (1 + annual_return)
        investments.append((year, investment_value))
    
    return investments

# Simulate investments
top_10_investments = simulate_investment(top_10)
middle_10_investments = simulate_investment(middle_10)
bottom_10_investments = simulate_investment(bottom_10)

# Debug: Check the investment simulation values
print("Top 10 Investments")
print(top_10_investments)
print("Middle 10 Investments")
print(middle_10_investments)
print("Bottom 10 Investments")
print(bottom_10_investments)

# Convert to DataFrame for visualization
investment_df = pd.DataFrame({
    'Year': [i[0] for i in top_10_investments],
    'Top 10': [i[1] for i in top_10_investments],
    'Middle 10': [i[1] for i in middle_10_investments],
    'Bottom 10': [i[1] for i in bottom_10_investments]
})
investment_df.set_index('Year', inplace=True)

# Plot the investment performance
plt.figure(figsize=(14, 7))
plt.plot(investment_df.index, investment_df['Top 10'], label='Top 10 Stocks')
plt.plot(investment_df.index, investment_df['Middle 10'], label='Middle 10 Stocks')
plt.plot(investment_df.index, investment_df['Bottom 10'], label='Bottom 10 Stocks')
plt.xlabel('Year')
plt.ylabel('Investment Value')
plt.title('Investment Performance Over Time')
plt.legend()
plt.show()
