import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol (NVDA for NVIDIA Corporation)
stock_symbol = "NVDA"

# Define the date range for the stock data
start_date = "2023-01-04"
end_date = "2023-10-01"

# Fetch stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate MACD and Signal Line
stock_data['12-day EMA'] = stock_data['Close'].ewm(span=12, adjust=False).mean()
stock_data['26-day EMA'] = stock_data['Close'].ewm(span=26, adjust=False).mean()
stock_data['MACD'] = stock_data['12-day EMA'] - stock_data['26-day EMA']
stock_data['Signal Line'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot MACD and Signal Line on the first subplot
ax1.plot(stock_data.index, stock_data['MACD'], label='MACD', color='blue')
ax1.plot(stock_data.index, stock_data['Signal Line'], label='Signal Line', color='orange')
ax1.bar(stock_data.index, stock_data['MACD'] - stock_data['Signal Line'], label='Histogram', color='purple')
ax1.set_title(f"MACD and Signal Line for {stock_symbol} Stock")
ax1.set_ylabel("Value")
ax1.legend()
ax1.grid()

# Plot Stock Price on the second subplot
ax2.plot(stock_data.index, stock_data['Close'], label='Stock Price', color='green')

# Convert the date string to a pandas Timestamp object
purchase_date = pd.Timestamp('2023-08-30')

# Add a red vertical line on August 30th
ax2.axvline(x=purchase_date, color='red', linestyle='--', label='Call Option Purchase')

ax2.set_title(f"Stock Price for {stock_symbol} Stock")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price")
ax2.legend()
ax2.grid()

plt.tight_layout()
plt.show()
