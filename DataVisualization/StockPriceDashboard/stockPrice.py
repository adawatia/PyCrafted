# Import necessary libraries
import yfinance as yf  # Yahoo Finance API for fetching stock market data
import streamlit as st  # Streamlit for creating interactive web apps
import pandas as pd  # Pandas for data manipulation (not used in this example)

# Display a header in the Streamlit app
st.header("Stock Price Dashboard")

# Define the stock ticker symbol (GOOGL represents Alphabet Inc., Google's parent company)
ticker_symbol = 'GOOGL'

# Fetch stock data using the Yahoo Finance API
ticker_data = yf.Ticker(ticker_symbol)

# Get historical market data for the specified period
# 'period' = '1d' means data is retrieved on a daily basis
# 'start' and 'end' define the date range for historical data
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2013-5-31')

# Display a subheader for closing price visualization
st.subheader("Close")
# Plot the closing price of the stock over time using a line chart
st.line_chart(ticker_df.Close)

# Display a subheader for trading volume visualization
st.subheader("Volume")
# Plot the trading volume of the stock over time using a line chart
st.line_chart(ticker_df.Volume)
