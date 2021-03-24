import streamlit as st
import yfinance as yf
import pandas as pd

# Setting the page config
st.set_page_config(page_title='Stock Price App', page_icon='chart_with_upwards_trend', layout='wide')

######################
# Page Title
######################

st.write('''
# Simple Stock Price App
The stock closing price and volume of Google
***
''')

######################
# Main Page
######################

google = yf.Ticker('GOOGL')
tickerDf = google.history(period='1d', start='2015-5-31', end='2017-5-31')

# Business Summary
st.write('''
## Business Summary
''')

st.write(google.info['longBusinessSummary'])

# Closing Price
st.write('''
## Closing Price
''')

st.line_chart(tickerDf.Close)

# Volume
st.write('''
## Volume
''')

st.line_chart(tickerDf.Volume)
