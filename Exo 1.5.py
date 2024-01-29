#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:22:18 2024

@author: jovana
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Downloading S&P 500 futures data
ticker = "ES=F"  # S&P 500 front-month futures ticker symbol 
data = yf.download(ticker)
values = data['Adj Close']

# Calculate arithmetic & logarithmic returns
arithmetic_returns = values.pct_change()
log_returns = np.log(values / values.shift(1))

# Add the returns to the DataFrame
sp500_data = pd.DataFrame(data)
sp500_data['Arithmetic Returns'] = arithmetic_returns
sp500_data['Logarithmic Returns'] = log_returns

# Display the DataFrame with returns
print(sp500_data.head())

# Calculating cumulative arithmetic and cumulative logarithmic returns
cumulative_arithmetic_return = np.cumsum(arithmetic_returns)
cumulative_logarithmic_return = np.exp(np.cumsum(log_returns)) - 1

plt.plot(cumulative_arithmetic_return, label='Cumulative Arithmetic Returns', marker='o')
plt.plot(cumulative_logarithmic_return, label='Cumulative Logarithmic Returns', marker='x')
plt.title('Cumulative Arithmetic vs. Logarithmic Returns')
plt.xlabel('Year')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.show()


# Comments :

# We can see the arithmetic returns are less volatile than logarithmic ones, which seem to 
# reflect better high market volatility periods.
# Both measures reflect the upward trend since 2000 as well as drawdowns from different crisis.
# Markets seem to have quickly recovered from drawdowns, as the response from investor predicted a quick recovery.